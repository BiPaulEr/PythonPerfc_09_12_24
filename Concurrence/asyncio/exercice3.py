import asyncio
import random
import time

async def do_work(duration):
    await asyncio.sleep(duration)
    jesuisunficntionsynchrone()
    return f"Finished work in {duration} seconds"

def jesuisunficntionsynchrone():
    time.sleep(4)


async def main():
    durees = [6, 2, 8, 4]
    tasks = [do_work(duration) for duration in durees]
    for future in asyncio.as_completed(tasks):
        result = await future
        print(f"Résultat {result}")


asyncio.run(main())