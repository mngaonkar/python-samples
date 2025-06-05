# Run multiple tasks concurrently using asyncio

import asyncio

async def task1():
    print("Task 1 is running")
    return "Result from Task 1"

async def task2():
    print("Task 2 is running")
    return "Result from Task 2"


def main():
    print("Hello, World!")

    # Create an event loop
    loop = asyncio.get_event_loop()
    
    # Create a task to run the coroutine
    task1_id = loop.create_task(task1())
    task2_id = loop.create_task(task2())

    pending = asyncio.all_tasks(loop)   
    print(f"Pending tasks: {pending}")

    group = asyncio.gather(task1_id, task2_id)
    loop.run_until_complete(group)
    print("All tasks completed.")

    # Close the event loop
    loop.close()

if __name__ == "__main__":
    main()