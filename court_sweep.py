import asyncio
from playwright.async_api import async_playwright

OUTPUT_FILE = r"C:\Users\Lance\pam_archive\data\Sang_Lee_Litigation.txt"
TARGET_URL = "https://odysseyportal.courts.wa.gov/odyportal/Home/Dashboard/29" # Skagit County Portal Node

async def execute_court_sweep():
    print("[*] Initializing WA State Court Node...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False) # Headless=False required to bypass initial portal bot-checks
        context = await browser.new_context()
        page = await context.new_page()
        
        try:
            await page.goto(TARGET_URL)
            print("[*] Portal accessed. Manual input required for CAPTCHA/Terms acceptance if prompted.")
            # Note: Odyssey Portal requires manual interaction for name queries. 
            # Instructing local agent to stage the environment.
            print("[!] INSTRUCTION: Search 'Lee, Sang' in the Smart Search bar. Filter by 'Skagit'.")
            
            for i in range(20): # 10 minutes total, check every 30s
                await page.screenshot(path="C:\\Users\\Lance\\Watchtower_Ops\\court_snapshot.png")
                print(f"[*] Snapshot {i+1} captured.")
                await asyncio.sleep(30)
        except Exception as e:
            print(f"[!] Target access failure: {e}")
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(execute_court_sweep())
