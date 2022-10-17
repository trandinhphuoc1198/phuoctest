import socket,time
ip=socket.gethostbyname(socket.gethostname())
port=9999
conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
conn.connect(('localhost',9999))

conn.send(b'hello')