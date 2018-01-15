import socket 

asocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

asocket.bind(('',80))
asocket.listen(5)

conn, addr = asocket.accept()
while True:
    data = conn.recv(1000)
    if not data:
        break
    print("Got a request!")

conn.close()
asocket.close()
