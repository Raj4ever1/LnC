import socket,time
from threading import Thread

def clientSection(conn,addr):
    print('Client connected: ', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        time.sleep(1)
        conn.sendall(data)

HOST = '127.0.0.1'
PORT = 5005
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(2)
while True :
    conn, addr = s.accept()
    Thread(target=clientSection,args=(conn,addr)).start() 