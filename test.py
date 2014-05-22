import socket




server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('', 7000))
server.listen(5)

while True:
    s, (ip, port) = server.accept()
    data = ''
    data = s.recv(10000)
    print data
    s.send("your page")
    s.close()

