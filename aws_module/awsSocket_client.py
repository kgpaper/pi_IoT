import socket 

def toPi(msg):
    HOST = '0.0.0.0'
    PORT = 10000
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    client_socket.connect((HOST, PORT))

    client_socket.send(msg.encode()) 
    data = client_socket.recv(1024) 
    print('Received from the server :',repr(data.decode())) 

    client_socket.close() 
    return data.decode()

def connectStatus():
    status = {'light':'', 'blind':''}
    print(toPi('light'))
    status['light'] = 'l'
    print(status)
    status['light'] = toPi('light')
    status['blind'] = toPi('blind')
    return status