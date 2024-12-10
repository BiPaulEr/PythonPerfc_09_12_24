import asyncio
from random import randint
import time

def traitement_du_result(msg):
    time.sleep(1)  #smbolise traitement cpu lourd
    print(msg)

async def worker(name):
    sleep_time = randint(1, 10)
    print(f" {name} : Begin Tasks for {sleep_time}s")
    await asyncio.sleep(sleep_time)
    print(f" {name} : End Tasks")
    return (f" {name} : Ouf j'ai entendu {sleep_time}s")

async def main():  
    for task in asyncio.as_completed((worker("w1"), worker("w2"),worker("w3"), worker("w4"), worker("w5"))):
        result = await task
        traitement_du_result(result)
    
asyncio.run(main())