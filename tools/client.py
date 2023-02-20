import socket

HOST = '127.0.0.1'
PORT = 5005
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print('Client connected.')
while True:
    user_input = str(input())
    if not user_input:
        break
    
    s.sendall(user_input.encode())
    data = s.recv(1024)
    if not data:
        break
    print("Data received from server: ", data.decode('utf-8'))