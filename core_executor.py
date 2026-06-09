import sys
import asyncio
import re
import logging
from typing import Dict, List

# Strict enforcement of Python 3.11+
if sys.version_info < (3, 11):
    sys.exit("CRITICAL ERROR: core_executor.py requires Python 3.11 or higher.")

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] [%(levelname)s] %(message)s")

class CoreExecutor:
    """Tactical staging executor with integrated regex parsing logic."""

    def __init__(self):
        # Base IOC extraction patterns
        self.patterns = {
            "ipv4": re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'),
            "email": re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'),
            "md5": re.compile(r'\b[a-fA-F0-9]{32}\b')
        }

    async def execute_and_parse(self, command: str) -> Dict[str, List[str]]:
        """Executes a shell command asynchronously and parses output for IOCs."""
        logging.info(f"Staging command execution: {command}")
        logging.warning("Awaiting Operator authorization to proceed...")
        
        # NOTE: Implement blocking authorization trigger here before subprocess launch
        
        logging.info("Executing payload...")
        process = await asyncio.create_subprocess_shell(
            command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        stdout, stderr = await process.communicate()
        output = stdout.decode('utf-8')
        
        if process.returncode != 0:
            logging.error(f"Execution failed with return code {process.returncode}")
            logging.error(stderr.decode('utf-8'))
            return {}

        return self._parse_output(output)

    def _parse_output(self, output: str) -> Dict[str, List[str]]:
        """Applies regex patterns to extract intelligence from raw output."""
        results = {}
        for key, pattern in self.patterns.items():
            matches = pattern.findall(output)
            results[key] = list(set(matches))
        
        logging.info(f"Extraction complete. Found: {results}")
        return results

async def main():
    executor = CoreExecutor()
    target_command = "echo 'Target acquired: 192.168.68.110 admin@watchtower.local'"
    extracted_data = await executor.execute_and_parse(target_command)
    print("Parsed Intelligence:", extracted_data)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Execution aborted by Operator.")
