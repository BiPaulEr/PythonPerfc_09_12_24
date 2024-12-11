import asyncio
import aiofiles

async def main():  
    async with aiofiles.open("./Concurrence/compte.txt", "r") as file:
        content = await file.read()
        print(content)

asyncio.run(main())