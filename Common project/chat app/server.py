import socket,select

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',9999))
s.setblocking(0)
s.listen(10)
connections=[]
while True:
    try:
        conn,addr=s.accept()
        connections.append(conn)
        print(f'{addr} entered the room!!')
    except:
        pass
    if connections:
        readers=select.select(connections,[],[],1)
        for client in readers[0]:
            try:
                data=client.recv(1024)
                msg=f'{client.getpeername()}>{data.decode()}'
            except:
                msg=f'{client.getpeername()} has quit the chat!!'
                connections.remove(client)
                print(msg)
            for conn in connections:
                conn.send(msg.encode())