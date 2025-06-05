# Future example using asyncio

from asyncio import Future
import asyncio
import time

async def main():
    f = Future()

    # Subscribe to future result
    def callback(future: Future):
        print(f"Future callback result: {future.result()}")
    f.add_done_callback(callback)

    print(f"is future done: {f.done()}")  # Output: is future done: False

    f.set_result("Hello, World!") # Set the result of the future
    await asyncio.sleep(1)  # Simulate some delay
    print(f.result())  # Output: Hello, World!
    print(f"is future done: {f.done()}")  # Output: is future done: True

if __name__ == "__main__":
    asyncio.run(main())

