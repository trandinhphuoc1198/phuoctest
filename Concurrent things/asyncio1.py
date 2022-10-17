import requests
import asyncio,aiohttp
import time 

def get(n):
    time.sleep(n+10)
    print(n)
    requests.get('http://example.com')
    print(f'"{n}done"')

async def get_async(n):
    return await asyncio.to_thread(get,n)

async def get_async(n):
    async with aiohttp.ClientSession() as session:
        print(n)
        response = await session.get('http://example.com')
        print(f'"{n}done"')
        

async def main():
    start = time.perf_counter()
    await asyncio.gather(*[get_async(n) for n in range(21)])
    print(f'Time took {time.perf_counter()-start}')

asyncio.run(main())


