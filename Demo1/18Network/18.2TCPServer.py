import socket
# 创建一个基于IPv4和TCP协议的Socket
import threading

import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定到本机,9999端口
s.bind(('127.0.0.1', 9999))

s.listen(5)
print('Waiting for connection...')


def tcplink(sock, addr):
    print('Accept new connect from  %s:%s... ' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello %s ' % data.decode('utf-8')).encode('utf-8'))

    sock.close()
    print('Disconnect from %s:%s...' % addr)

# accept()会等待并返回一个客户端的连接
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()












