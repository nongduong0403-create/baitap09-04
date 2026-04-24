import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 8092

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, SERVER_PORT))

# Yêu cầu người dùng nhập chuỗi mật khẩu
# Ví dụ nhập: Abc123@1,aF1#2w3E*,2We3345
data_input = input("Nhap cac mat khau (cach nhau boi dau phay): ")

# Gửi sang Server
client.send(data_input.encode('utf-8'))

# Nhận kết quả từ Server
result = client.recv(1024).decode('utf-8')

# In kết quả ra màn hình
print(f"Cac mat khau hop le: {result}")

client.close()