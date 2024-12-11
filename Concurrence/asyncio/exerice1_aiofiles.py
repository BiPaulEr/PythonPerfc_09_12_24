import asyncio
import aiofiles

async def write_file(filename, message):
    async with aiofiles.open(filename, "a") as file:
        await file.write(message)
    return True

async def read_file(filename):
    async with aiofiles.open(filename, "r") as file:
        result  = await file.read()
    return(f"Contents of {result}")

def on_file_processed(task):
    print(task.result())

async def main():
    liste_file = ["file1.txt", "file2.txt", "file3.txt"]
    tasks = []
    for file in liste_file:
        task = asyncio.create_task(read_file(file))
        task.add_done_callback(on_file_processed)
        tasks.append(task)
    
    for task in tasks:
        await task

asyncio.run(main())