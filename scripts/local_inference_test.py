import asyncio
import aiohttp

# Prerequisites: Ensure Ollama is installed and the 'gemma' model is pulled locally.
# Execute: pip install aiohttp

async def local_inference_engine(text: str, task: str) -> None:
    # Routes request to local Ollama instance running on OptiPlex or Tab A8
    url = "http://127.0.0.1:11434/api/generate"
    prompt = f"Instruction: Perform {task} on the following text. Output only the result.\nText: {text}"
    payload = {
        "model": "llama3", 
        "prompt": prompt, 
        "stream": False
    }

    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(url, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    print(f"[*] Task: {task}\n[*] Result:\n{data.get('response', '').strip()}\n")
                else:
                    print(f"[!] Local inference failed. HTTP Status: {response.status}")
        except Exception as e:
             print(f"[!] Connection error: Verify Ollama is actively running. Details: {e}")

async def main():
    target_data = "El objetivo principal se encuentra en Burlington, Washington."
    
    print("[*] Initiating local inference processing...\n")
    await asyncio.gather(
        local_inference_engine(target_data, "Translation to English"),
        local_inference_engine(target_data, "Entity Extraction (identify locations and names)")
    )

if __name__ == "__main__":
    asyncio.run(main())