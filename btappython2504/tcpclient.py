import socket

# 1. Cấu hình (Phải khớp với Server)
SERVER_IP = "127.0.0.1"
SERVER_PORT = 8090

# 2. Tao Socket TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3. Ket noi den Server
client.connect((SERVER_IP, SERVER_PORT))

# 4. Gui thong diep
message = "From CLIENT TCP"
client.send(message.encode('utf-8'))
print(f"Da gui: {message}")

# 5. Nhan phan hoi tu Server
data = client.recv(1024).decode('utf-8')
print(f"Server phan hoi: {data}")

# 6. Dong ket noi
client.close()