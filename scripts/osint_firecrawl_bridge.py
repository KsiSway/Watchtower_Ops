import asyncio
import aiohttp
import random
import sys
import json
import os
from dotenv import load_dotenv

# The Turnstile: Strictly limits concurrency to 5 active network sockets
CONCURRENCY_LIMIT = 5
semaphore = asyncio.Semaphore(CONCURRENCY_LIMIT)

async def fetch_target(session, url, max_retries=3):
    # The lock prevents execution until a slot in the semaphore opens
    async with semaphore:
        for attempt in range(max_retries):
            try:
                async with session.get(url) as response:
                    # Automated Exponential Backoff for Rate Limiting
                    if response.status == 429:
                        sleep_time = (2 ** attempt) + random.uniform(0, 1) # Jitter
                        print(f"[!] HTTP 429 Rate Limit on {url}. Backing off for {sleep_time:.2f}s")
                        await asyncio.sleep(sleep_time)
                        continue
                    
                    if response.status == 200:
                        print(f"[+] Extraction complete: {url}")
                        return await response.text()
                        
            except aiohttp.ClientError as e:
                print(f"[-] Network fault on {url}: {e}")
                break
                
        return None

async def extraction_pipeline(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_target(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

if __name__ == "__main__":
    load_dotenv()
    if len(sys.argv) > 1:
        target_file = sys.argv[1]
        with open(target_file, "r") as f:
            urls = [line.strip() for line in f if line.strip()]
        
        asyncio.run(extraction_pipeline(urls))
