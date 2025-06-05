# Difference between a function and a coroutine
import asyncio

async def hello_world():
    print("Hello, World!")

print(f"type of hello_world: {type(hello_world)}")
print(f"is hello_world coroutine: {asyncio.iscoroutinefunction(hello_world)}")

# Note, function invocation returns coroutine object
print(f"type of hello_world(): {type(hello_world())}") 

def greet(name: str) -> str:
    return f"Hello, {name}!"

print(f"type of greet: {type(greet)}")

# Note, function invocation returns string (return value)
print(f"type of greet(): {type(greet('World'))}")