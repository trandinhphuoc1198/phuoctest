import socket,asyncio,time

s = socket.socket()
s.bind(('localhost',90))
s.listen(50)

connections = []

for i in range(2):
    connection = s.accept()
    print(f'New connection from {connection[1]}')
    connections.append(connection)

def receiver(connection):
    while True:
        data = connection[0].recv(1024)
        print(f'Received from {connection[1]}: {data}')


async def async_receiver(conn):
    return await asyncio.to_thread(receiver,conn)

async def main():
        await asyncio.gather(*[async_receiver(conn) for conn in connections])

asyncio.run(main())