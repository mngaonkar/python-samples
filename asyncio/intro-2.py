# Asyncio hello world example that blocks the event loop

import asyncio
import time

async def main():
    time.sleep(1)  # This will block the event loop
    print("Hello, World!")

asyncio.run(main())

