import asyncio
import time

def info(task):
    print(f"Task Annule : {task.cancelled()}")
    print(f"Task Terminé : {task.done()}")
    if (task.done()):
        print(f"Task Résutat : {task.result()}")
        print(f"Task Exception : {task.exception()}")

async def worker(name, sleep_time):
    print(f" {name} : Begin Tasks for {sleep_time}s")
    await asyncio.sleep(sleep_time)
    print(f" {name} : End Tasks")
    return (f" {name} : Ouf j'ai entendu {sleep_time}s")

async def main():  
    w1 = asyncio.create_task(worker("w1", 5))
    info(w1)
    w2 = asyncio.create_task(worker("w2", 5))

    await w1
    info(w1)
    
    await w2
    print("MT : j'ai attendu assez pour w2")

asyncio.run(main())