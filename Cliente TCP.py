import socket

ip = "127.0.0.1"
porta = 8080

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((ip, porta))

while True:
	dados = soc.recv(1024)
	print(f"mensagem recebida: {dados}")
	dadosinput = input("msg~# ")
	soc.send(str.encode(dadosinput))
