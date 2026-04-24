import socket

# Cấu hình IP và Port của Server cần kết nối tới
SERVER_IP = "127.0.0.1"
SERVER_PORT = 8091

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Client sử dụng lệnh connect() để kết nối
client.connect((SERVER_IP, SERVER_PORT))

# Nhập số từ bàn phím
a = input("Nhap so nguyen a: ")
b = input("Nhap so nguyen b: ")

# Gửi 2 số sang server dưới dạng chuỗi "a,b"
message = f"{a},{b}"
client.send(message.encode('utf-8'))

# Nhận kết quả tổng từ Server
result = client.recv(1024).decode('utf-8')
print(f"Ket qua tong tu Server tra ve: {result}")

client.close()