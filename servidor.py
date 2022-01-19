import socket

#host e port
host = "localhost"
port = 8888

#porta aberta e obtendo a conexão
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen()
print(f"Esperando conexao de algum host ...")
conectado, hst = sock.accept()
print(f"\nConexao foi feita:")
print(f"\nHOST => {hst}")
print(f"STATUS => conectado")

contador = 0
while True:
	dados = conectado.recv(1024)
	print(f"Mensagem recebida => {dados}")
	if not dados:
		print("\n\nConexâo da conexão => {fechada}")
		conectado.close()
		break
	if contador == 0:
		contador = 1
		recvmsg = "mensagem recebida, conexao foi feita com sucesso!"
		conectado.sendall(str.encode(recvmsg))
