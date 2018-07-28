import socket

client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 8820))

client_socket.send('Omer')
data = client_socket.recv(1024)
print('You sent to the server:  ' + data)

client_socket.close()
