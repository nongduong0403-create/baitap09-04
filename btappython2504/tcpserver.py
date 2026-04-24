import socket

# 1. Cấu hình địa chỉ và cổng
IP = "127.0.0.1"
PORT = 8090

# 2. Tạo Socket TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3. Gắn IP và Port vào Socket
server.bind((IP, PORT))

# 4. Bắt đầu lắng nghe (tối đa 1 kết nối chờ)
server.listen(1)
print(f"--- SERVER DANG CHAY TAI {IP}:{PORT} ---")

while True:
    # 5. Chấp nhận kết nối từ Client
    client_conn, addr = server.accept()
    print(f"Co ket noi tu: {addr}")

    # 6. Nhận dữ liệu (tối đa 1024 bytes) và giải mã
    data = client_conn.recv(1024).decode('utf-8')
    print(f"Client gui: {data}")

    # 7. Gui phan hoi lai cho Client
    response = "From SERVER TCP"
    client_conn.send(response.encode('utf-8'))

    # 8. Dong ket noi voi Client nay
    client_conn.close()