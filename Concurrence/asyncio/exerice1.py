import asyncio

async def read_file(file_name):
    await asyncio.sleep(1)  # Simulate the delay of reading a file
    print(f"{file_name} read successfully")
    return(f"Contents of {file_name}")

async def main():
    liste_file = ["data/file1.txt", "data/file2.txt", "data/file3.txt"]
    tasks = []
    for file in liste_file:
        task = asyncio.create_task(read_file(file))
        tasks.append(task)
    
    for task in tasks:
        await task
        print(task.result())

asyncio.run(main())