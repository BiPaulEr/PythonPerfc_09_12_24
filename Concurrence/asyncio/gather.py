import asyncio
import time

def print_task(task):
    print(task.result())
    

async def worker(name, sleep_time):
    print(f" {name} : Begin Tasks for {sleep_time}s")
    await asyncio.sleep(sleep_time)
    print(f" {name} : End Tasks")
    return (f" {name} : Ouf j'ai entendu {sleep_time}s")

async def main():  
    result = await asyncio.gather(worker("w1", 5), worker("w2", 5))
    print(result)



asyncio.run(main())