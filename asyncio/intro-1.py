# Thread example instead of asyncio

from concurrent.futures import ThreadPoolExecutor

def hello(data: str):
    print(f"Hello {data} from the thread!")

with ThreadPoolExecutor() as executor:
    future1 = executor.submit(hello, "World")
    future12= executor.submit(hello, "Universe")
    # Wait for the thread to complete
    future1.result()
    future12.result()
    print("Thread has completed execution.")