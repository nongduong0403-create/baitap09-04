import socket

# Khai báo IP và Port ở ngay đầu tiên (Đây chính là dòng bạn bị thiếu)
IP = "127.0.0.1"
PORT = 8091

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(1)

print(f"--- SERVER TINH TONG DANG CHAY TAI PORT {PORT} ---")

while True:
    conn, addr = server.accept()
    
    # Nhận chuỗi dữ liệu (ví dụ: "10,20")
    data = conn.recv(1024).decode('utf-8')
    
    if data:
        # Tách chuỗi thành 2 số nguyên
        nums = data.split(',')
        a = int(nums[0])
        b = int(nums[1])
        
        tong = a + b
        print(f"Nhan tu Client: a={a}, b={b}. Tong la: {tong}")
        
        # Gửi kết quả về (phải đổi số thành chuỗi mới gửi được)
        conn.send(str(tong).encode('utf-8'))
    
    conn.close()