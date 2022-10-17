import socket,time,json
IP='localhost'
port=9999
s=socket.socket()
s.bind((IP,port))
s.listen(1)
conn,addr=s.accept()
nn=0
while True:
    nn+=1
    a=conn.recv(350)
    print(nn)
conn.send(json.dumps({'hi':123}).encode('utf-8'))
response="HTTP/1.2 400 OK\r\nContent-Length: 100\r\nContent-Type: application/json\r\n\r\n"
conn.send(response.encode('utf-8'))