import socket

HOST = "localhost" ## ou 127.0.0.1
PORT = 7778

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print("Aguardando Cliente")
conn, ender = s.accept()

print("conectando em", ender)
while True:
    data = conn.recev(1024)
    if not data:
        print("Fechando a conexão")
        conn.close()
        break
    conn.sendall(data)
    