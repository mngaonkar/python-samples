# Run task that calls a blocking function

import asyncio

def create_message(messsage: str) -> str:
    return f"Message: {messsage}"

async def hello_world():
    print(create_message("Hello, World!"))

def main():
    print("Hello, World!")

    # Create an event loop
    loop = asyncio.get_event_loop()
    
    # Create a task to run the coroutine
    task = loop.create_task(hello_world())
    print(f"Task created: {task}")
    
    # Run the event loop until the task is complete
    loop.run_until_complete(task)

    # Close the event loop
    loop.close()

if __name__ == "__main__":
    main()