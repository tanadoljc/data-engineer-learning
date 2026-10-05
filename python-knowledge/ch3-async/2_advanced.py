import asyncio

async def process1():
    print("Process-1 Start")
    await asyncio.sleep(6)
    print("Process-1 End")

async def process2():
    print("Process-2 Start")
    await asyncio.sleep(6)
    print("Process-2 End")

async def main():
    # same event loop
    await asyncio.gather(process1(), process2())

asyncio.run(main())
