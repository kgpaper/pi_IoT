import socket 

def connectPi(msg):
    HOST = '0.0.0.0'
    PORT = 10000
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    client_socket.connect((HOST, PORT))

    client_socket.send(msg.encode()) 
    data = client_socket.recv(1024) 
    print('Received from the server :',repr(data.decode())) 

    client_socket.close() 

connectPi('123')