from socket import *
from select import *
import blindControl

HOST = ''
PORT = 10000
BUFSIZE = 1024
ADDR = (HOST, PORT)

# 소켓 생성
serverSocket = socket(AF_INET, SOCK_STREAM)

# 소켓 주소 정보 할당
serverSocket.bind(ADDR)
print('bind')

# 연결 수신 대기 상태
serverSocket.listen(100)
print('listen')

# 연결 수락
clientSocekt, addr_info = serverSocket.accept()
print('accept')
print('--client information--')
print(clientSocekt)

# 클라이언트로부터 메시지를 가져옴
while True:
    data = clientSocekt.recv(65535)
    print('recieve data : ',data.decode())
    msg = data.decode()
    if msg == 'blind'
    if msg == 'exit': # exit라는 메세지를 받으면 종료
        break

# 소켓 종료
clientSocekt.close()
serverSocket.close()
print('close')