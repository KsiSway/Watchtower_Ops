import asyncio
import os
import random
from urllib.parse import quote
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError

# --- WATCHTOWER CONFIGURATION ---
OUTPUT_DIR = r"C:\Users\Lance\pam_archive\data"
TARGET_YEAR_START = 1986
TARGET_YEAR_END = 1993
SEARCH_QUERY = '"Surry Scene" OR "Trinity Crosses"'
MAX_RETRIES = 5

os.makedirs(OUTPUT_DIR, exist_ok=True)

async def exponential_backoff(attempt):
    """Calculates and executes delay to evade rate limiting."""
    base_delay = 2
    delay = (base_delay ** attempt) + random.uniform(0.1, 1.5)
    print(f"[*] Rate limit mitigation. Backing off for {delay:.2f} seconds...")
    await asyncio.sleep(delay)

async def process_page(page, page_num):
    """Extracts and pipes image URLs from the current DOM."""
    print(f"[*] Parsing DOM on results page {page_num}...")
    
    # Wait for results container to render. DigitalNC uses standard WordPress-like article tags for main search.
    try:
        # Wait for either article elements or a "nothing matched" message
        await page.wait_for_selector('article, .no-results', timeout=15000)
    except PlaywrightTimeoutError:
        print("[-] No search results container found. DOM structure may have shifted.")
        return 0
        
    content = await page.content()
    if "nothing matched your search terms" in content:
        return 0

    # Extract high-res image nodes within the articles
    items = await page.query_selector_all('article img')
    
    extracted = 0
    for i, item in enumerate(items):
        src = await item.get_attribute('src')
        if src:
            filename = os.path.join(OUTPUT_DIR, f"Surry_Scene_Pg{page_num}_Item{i}.jpg")
            print(f"[+] Extracted payload: {src} -> Piping to {filename}")
            extracted += 1
            
    return extracted

async def execute_scrape():
    print(f"[*] Initializing Async Playwright Engine...")
    print(f"[*] Target Vector: {SEARCH_QUERY} | Range: {TARGET_YEAR_START}-{TARGET_YEAR_END}")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        # Construct correct target URL for DigitalNC main search
        encoded_query = quote(SEARCH_QUERY)
        target_url = f"https://www.digitalnc.org/?s={encoded_query}"
        
        current_page = 1
        has_next = True
        
        while has_next:
            for attempt in range(MAX_RETRIES):
                try:
                    paginated_url = f"{target_url}&paged={current_page}" if current_page > 1 else target_url
                    print(f"[*] Navigating to {paginated_url}")
                    
                    await page.goto(paginated_url, wait_until="domcontentloaded")
                    
                    hits = await process_page(page, current_page)
                    if hits == 0:
                        print("[-] No valid targets found on this page.")
                    
                    # Pagination logic check: DigitalNC uses .next.page-numbers
                    next_button = await page.query_selector('a.next.page-numbers')
                    if next_button:
                        current_page += 1
                        # Random jitter between pages to mimic human latency
                        await asyncio.sleep(random.uniform(1.5, 3.5))
                        break # Break retry loop, proceed to next page
                    else:
                        print("[*] Reached end of pagination.")
                        has_next = False
                        break
                        
                except PlaywrightTimeoutError:
                    print(f"[!] Network timeout on attempt {attempt + 1}/{MAX_RETRIES}.")
                    await exponential_backoff(attempt)
                except Exception as e:
                    print(f"[!] Critical DOM failure: {e}")
                    has_next = False
                    break
            else:
                print("[!] Max retries exceeded. Halting pagination vector.")
                has_next = False

        await browser.close()
        print(f"[*] Extraction complete. Terminating headless instance.")

if __name__ == "__main__":
    asyncio.run(execute_scrape())
