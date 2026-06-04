import asyncio
from urllib.parse import quote
from playwright.async_api import async_playwright

# --- WATCHTOWER CONFIGURATION ---
OUTPUT_FILE = r"C:\Users\Lance\pam_archive\data\Mt_Airy_Recon.txt"

# Localized Dorks targeting the Mount Airy / Surry County vector
DORKS = [
    'site:mtairynews.com "Surry Scene" OR "Pam Sykes"',
    'site:facebook.com "Mount Airy" "Surry Scene"',
    'site:genealogy.com "Charles Aaron Sykes" OR "Pamela Jean Sykes"',
    'site:surry.net "Sykes" OR "Trinity Crosses"',
    '"Sykes Brothers Dairy" "Mount Airy" NC'
]

async def execute_mt_airy_sweep():
    print("[*] Initializing Playwright Engine for Mount Airy Recon...")
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("--- MOUNT AIRY OSINT RECONNAISSANCE ---\n\n")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        for dork in DORKS:
            print(f"[*] Executing target vector: {dork}")
            # Utilizing DuckDuckGo HTML version to bypass aggressive Google CAPTCHAs during automated dorking
            target_url = f"https://duckduckgo.com/html/?q={quote(dork)}"
            
            try:
                await page.goto(target_url, wait_until="domcontentloaded")
                await asyncio.sleep(2.5) # Exponential backoff bypass logic
                
                results = await page.query_selector_all('.result__snippet')
                links = await page.query_selector_all('.result__url')
                
                with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
                    f.write(f"QUERY: {dork}\n")
                    if not results:
                        f.write("[-] Null response for this vector.\n\n")
                    
                    for i in range(len(results)):
                        snippet_text = await results[i].inner_text()
                        link_text = await links[i].inner_text() if i < len(links) else "Unknown URL"
                        f.write(f"URL: {link_text}\nDATA: {snippet_text}\n---\n")
                    f.write("\n")
            except Exception as e:
                print(f"[!] Error processing vector {dork}: {e}")

        await browser.close()
        print(f"[*] Recon sweep complete. Data piped to {OUTPUT_FILE}")

if __name__ == "__main__":
    asyncio.run(execute_mt_airy_sweep())
