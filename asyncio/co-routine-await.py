import asyncio


async def add(x: int, y: int) -> int:
    """A simple function to add two numbers."""
    return x + y

async def main():
    result = await add(1, 2)  # Await the coroutine to get the result
    print(f"Result of addition: {result}")  # Print the result

if __name__ == "__main__":
    asyncio.run(main())  # Run the main coroutine using asyncio.run