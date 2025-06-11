""" Example of coverting a blocking function to be used in an async context using run_in_executor. """
import asyncio
import requests
from contextlib import asynccontextmanager

def download_url(url: str) -> str:
    response = requests.get(url)
    return response.text

@asynccontextmanager
async def process_url(url: str):
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, download_url, url)
    try:
        yield result
    finally:
        print(f"Finished processing {url}")

async def main():
    url = "http://www.google.com"
    async with process_url(url) as result:
        print(f"Downloaded content from {url}: {result[:100]}...")

if __name__ == "__main__":
    asyncio.run(main())