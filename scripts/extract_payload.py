import asyncio
import urllib.request
from html.parser import HTMLParser

# Utilizes standard libraries only; compatible natively with ARM64 and x64 architectures.

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text_data = []

    def handle_data(self, data):
        cleaned = data.strip()
        if cleaned:
            self.text_data.append(cleaned)

async def fetch_and_extract(url: str) -> None:
    print(f"[*] Fetching target: {url}")
    loop = asyncio.get_running_loop()
    
    try:
        # Execute blocking network call in default executor
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = await loop.run_in_executor(None, urllib.request.urlopen, req)
        html_content = response.read().decode('utf-8')
        
        extractor = TextExtractor()
        extractor.feed(html_content)
        
        output_file = "extracted_payload.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(extractor.text_data))
            
        print(f"[+] Extraction complete. Payload saved to {output_file}. Ready for NotebookLM upload.")
    except Exception as e:
        print(f"[-] Execution failed: {e}")

if __name__ == "__main__":
    target_url = input("Enter target URL for extraction: ")
    asyncio.run(fetch_and_extract(target_url))