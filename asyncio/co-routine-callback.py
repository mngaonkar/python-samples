# Create tasks with callbacks using asyncio

import asyncio

async def add(x: int, y: int) -> int:
    """A simple function to add two numbers."""
    return x + y

async def main():
    add_coro = asyncio.create_task(add(1, 2))  # Create the coroutine object
    add_coro.add_done_callback(lambda fut: print(f"Callback: {fut.result()}"))  # Add a callback to be called when the coroutine is done
    asyncio.sleep(3)  # Simulate some delay before checking the result
    print(f"Is coroutine done: {add_coro.done()}")  # Check if the coroutine is done
    
    await add_coro  # Await the coroutine to get the result
    print(f"Result of addition: {add_coro.result()}")  # Print the result

if __name__ == "__main__":
    # Run the main coroutine using asyncio.run
    asyncio.run(main())