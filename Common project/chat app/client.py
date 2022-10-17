import msvcrt,socket,select
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost',9999))
msg=''
while True:
    reader=select.select([client],[],[],.1)
    for from_ser in reader[0]:
        data=from_ser.recv(1024).decode('utf-8')
        print(data)
    if msvcrt.kbhit():
        key=msvcrt.getche().decode('utf-8')
        if key=='\r':
            if msg=='quit':
                break
            client.send(msg.encode())
            msg=''
            print()
        else:
            msg+=key