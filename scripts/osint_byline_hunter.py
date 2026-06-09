import asyncio
import json
from playwright.async_api import async_playwright

async def scrape_byline_metadata():
    url = "https://www.surrydigitalheritage.org/s/surry-digital-heritage/item?Search=Surry+Scene"
    results = []
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        print(f"[*] Navigating to Surry Digital Heritage: {url}")
        await page.goto(url, wait_until='domcontentloaded')
        
        # Extract item links
        items = await page.query_selector_all('ul.resource-list li.item h4 a')
        item_urls = [await item.get_attribute('href') for item in items]
        
        for item_url in item_urls[:10]: # Check first 10 items
            full_url = f"https://www.surrydigitalheritage.org{item_url}"
            print(f"[*] Checking item: {full_url}")
            await page.goto(full_url, wait_until='domcontentloaded')
            
            # Look for "Pam Sykes" or "Pamela Sykes" in metadata
            content = await page.content()
            if "Pam Sykes" in content or "Pamela Sykes" in content or "Sykes" in content:
                metadata = {}
                rows = await page.query_selector_all('.property')
                for row in rows:
                    label_el = await row.query_selector('h4')
                    value_el = await row.query_selector('.values')
                    if label_el and value_el:
                        label = await label_el.inner_text()
                        value = await value_el.inner_text()
                        metadata[label.strip()] = value.strip()
                
                results.append({"url": full_url, "metadata": metadata})
        
        await browser.close()
    return results

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    output = loop.run_until_complete(scrape_byline_metadata())
    print(json.dumps(output, indent=2))
