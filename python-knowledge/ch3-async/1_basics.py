import asyncio

async def process1():
    print("Process-1 Start")
    asyncio.sleep(6) # idle state then skip
    print("Process-1 End")

async def process2():
    print("Process-2 Start")
    await asyncio.sleep(6)
    print("Process-2 End")

# First Event Loop
asyncio.run(process1())

# Second Event Loop
asyncio.run(process2())
