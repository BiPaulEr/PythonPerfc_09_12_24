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
    w1 = asyncio.create_task(worker("w1", 5))
    w1.add_done_callback(print_task)
    
    w2 = asyncio.create_task(worker("w2", 5))
    w2.add_done_callback(print_task)

    await w1
    
    await w2


asyncio.run(main())