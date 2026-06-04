#!/usr/bin/env python3
# Minimum Requirement: Python 3.11+
# Dependency: Sherlock (https://github.com/sherlock-project/sherlock) or aiohttp for fallback

import asyncio
import json
import sys
import aiohttp

async def execute_fallback_sweep(alias: str) -> list:
    """Alternative fallback logic if the primary Sherlock vector fails."""
    high_value_targets = {
        "GitHub": f"https://github.com/{alias}",
        "Reddit": f"https://www.reddit.com/user/{alias}",
        "Pastebin": f"https://pastebin.com/u/{alias}",
        "HackerNews": f"https://news.ycombinator.com/user?id={alias}"
    }
    found_urls = []
    
    # Implementing basic request logic as fallback
    async with aiohttp.ClientSession() as session:
        for site, url in high_value_targets.items():
            try:
                async with session.get(url, timeout=5) as resp:
                    if resp.status == 200:
                        found_urls.append(url)
            except Exception:
                continue
    return found_urls

async def execute_footprint_bridge(target_alias: str):
    """Hunts an alias and pipes results to the offline Cognitive Brain."""
    
    try:
        # Step 1: Execute Primary Footprint Sweep
        sherlock_proc = await asyncio.create_subprocess_exec(
            "sherlock", target_alias, "--print-found", "--timeout", "5",
            stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await sherlock_proc.communicate()
        
        discovered_urls = []
        
        if sherlock_proc.returncode == 0:
            raw_output = stdout.decode().strip().split('\n')
            discovered_urls = [line.strip() for line in raw_output if "http" in line]
        else:
            # Step 1b: Automated Fallback Engagement
            discovered_urls = await execute_fallback_sweep(target_alias)

        if not discovered_urls:
            return {"status": "success", "analysis": "Zero footprint detected. Target alias is clean or highly disciplined."}

        # Step 2: Package raw data for the AI
        dossier = f"TARGET ALIAS: {target_alias}\nDISCOVERED NODES:\n" + "\n".join(discovered_urls)

        # Step 3: Pipe to local Cognitive Brain (osint_brain.py)
        brain_proc = await asyncio.create_subprocess_exec(
            "python", "osint_brain.py", "profile", dossier,
            stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        b_stdout, b_stderr = await brain_proc.communicate()

        if brain_proc.returncode != 0:
             return {"status": "error", "message": f"Brain pipeline failed: {b_stderr.decode().strip()}"}

        # Return the LLM's synthesized profile
        return json.loads(b_stdout.decode().strip())

    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Usage: python3 osint_sherlock_bridge.py <target_alias>"}))
        sys.exit(1)
        
    result = asyncio.run(execute_footprint_bridge(sys.argv[1]))
    print(json.dumps(result, indent=2))
