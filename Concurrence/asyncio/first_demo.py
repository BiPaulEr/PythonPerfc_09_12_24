import asyncio
import time

async def worker(name, sleep_time):
    print(f" {name} : Begin Tasks for {sleep_time}s")
    await asyncio.sleep(sleep_time)
    print(f" {name} : End Tasks")

async def main():  
    w1 = asyncio.create_task(worker("w1", 5))
    w2 = asyncio.create_task(worker("w2", 3))
    await w1
    print("MT : j'ai attendu assez pour w1")
    
    await w2
    print("MT : j'ai attendu assez pour w2")

asyncio.run(main())