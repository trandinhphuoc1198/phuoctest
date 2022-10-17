import asyncio,time


def read_file(x):
    time.sleep(1)
    print(x)
    f= open(f'{x}.txt','r') 
    data= f.read()
    print('done'+str(x))

async def read_file_async(x):
    return await asyncio.to_thread(read_file,x)

async def main():
    start = time.perf_counter()
    await asyncio.gather(*[read_file_async(x) for x in range(3)])
    print(f'{time.perf_counter()-start}')    

asyncio.run(main())