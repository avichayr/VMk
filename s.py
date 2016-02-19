import socket
s = socket.socket()
s.bind(('', 6789))

s.listen(3)
conn, addr = s.accept()
print 'connected'
print conn.recv(2048), addr
conn.close()
s.close()