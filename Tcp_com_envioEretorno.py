import socket

HOST = "192.168.0.2" ## ip  e porta do meu celular
PORT = 7778

s = socket.socket(socket.AF_INET, socket.SOCk_STREAM)
s.connect((HOST, PORT))
s.sendall(str.encode("Bom dia Mario Junior!"))
data = s.recv(1024)

print("Mensagem Retornada:", data.decode())

