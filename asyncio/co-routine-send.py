# Coroutine send example

import asyncio

async def add(x: int, y: int) -> int:
    print(f"Adding {x} and {y}")
    return x + y

add_coro = add(1, 2)
try:
    add_coro.send(None)  # Start the coroutine
except StopIteration as e: # StopIteration is raised when the coroutine completes
    print(f"Coroutine completed with result: {e.value}")

print(add_coro)