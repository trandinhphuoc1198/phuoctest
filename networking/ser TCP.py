import socket
from threading import Thread
connections=[]
ip=socket.gethostbyname(socket.gethostname())
port=9999
ser=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ser.bind(('localhost',port))
def connect():
    while True:
        ser.listen(10)
        conn,address=ser.accept()
        connections.append([conn,address])
def show_connection():
    print('Connection list:')
    for num,connection in enumerate(connections):
        print(f'{num}/ IP: {connection[1][0]} Port: {connection[1][1]}')
def delete_connection(connection):
    print(f'Deleting connect {connections[connection][1]}...')
    connections[connection][0].close()
    connections.pop(connection)
    print('Successful!!')
def send(conn):
    while True:
        print(connections[conn][0].recv(2048))
        text=input(f'send to {connections[conn][1]}: ')
        if text !='quit':
            try:
                connections[conn][0].send(text.encode('utf-8'))
            except:
                print('Cannot send message to the client, delete connection!')
                delete_connection(conn)
                break
        else:
            break
def control():
    while True:
        if connections:
            show_connection()
            conn=int(input('Choose the connection: '))
            print(f'What do you wanna do to {conn}:\n1. Send text\n2. Delete connection')
            choice=int(input('Your choice: '))
            if choice==1:
                send(conn)
            elif choice==2:
                delete_connection(conn)
        else:
            print('There no connection now!\nPress any key for reset')
            input()
t1=Thread(target=connect,daemon=True)
t2=Thread(target=control,daemon=True)
t2.start()
t1.start()
t2.join()
t1.join()
