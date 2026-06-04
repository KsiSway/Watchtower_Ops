import asyncio
from urllib.parse import quote
from playwright.async_api import async_playwright

# --- WATCHTOWER CONFIGURATION ---
OUTPUT_FILE = r"C:\Users\Lance\pam_archive\data\Skagit_Motel_Timeline.txt"

# Targeted Dorks to isolate the August 2023 closure and Sang Lee
DORKS = [
    'site:goskagit.com "Skagit Motel" "Sang Lee"',
    'site:skagitcounty.net "1862 State Route 20" OR "Skagit Motel"',
    'site:wa.gov "Skagit Motel" closure OR violation',
    '"Sang Lee" "Skagit Motel" eviction OR lawsuit'
]

async def execute_dork_sweep():
    print("[*] Initializing Playwright Engine for Skagit County Recon...")
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("--- SKAGIT MOTEL CLOSURE RECONNAISSANCE ---\n\n")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        for dork in DORKS:
            print(f"[*] Executing target vector: {dork}")
            # Utilizing a privacy-respecting search engine to avoid aggressive CAPTCHAs during automated dorking
            target_url = f"https://duckduckgo.com/html/?q={quote(dork)}"
            
            try:
                await page.goto(target_url, wait_until="domcontentloaded")
                await asyncio.sleep(2) # Exponential backoff bypass
                
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
    asyncio.run(execute_dork_sweep())
