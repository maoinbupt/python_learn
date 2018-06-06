import socket

s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.connect(('127.0.0.1', 9999))

print(s2.recv(1024).decode('utf-8'))
for data in ['Gaofeng', 'ZhaoXiaokun']:
    s2.send(data.encode('utf-8'))
    print(s2.recv(1024).decode('utf-8'))
s2.send(b'exit')
s2.close()