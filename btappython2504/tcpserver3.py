import socket
import re # Thư viện dùng để kiểm tra các mẫu chuỗi (chữ hoa, chữ thường, số...)

IP = "127.0.0.1"
PORT = 8092

# Hàm kiểm tra 1 mật khẩu có hợp lệ hay không
def is_valid_password(pwd):
    # 5 & 6. Kiểm tra độ dài từ 6 đến 12
    if len(pwd) < 6 or len(pwd) > 12:
        return False
    
    # 1. Ít nhất 1 chữ cái [a-z]
    if not re.search("[a-z]", pwd):
        return False
        
    # 2. Ít nhất 1 số [0-9]
    if not re.search("[0-9]", pwd):
        return False
        
    # 3. Ít nhất 1 chữ hoa [A-Z]
    if not re.search("[A-Z]", pwd):
        return False
        
    # 4. Ít nhất 1 ký tự đặc biệt [$ # @]
    if not re.search("[$#@]", pwd):
        return False
        
    # Nếu vượt qua hết các bài kiểm tra trên thì là hợp lệ
    return True

# Thiết lập Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(1)

print(f"--- SERVER KIEM TRA MAT KHAU DANG CHAY TAI PORT {PORT} ---")

while True:
    conn, addr = server.accept()
    
    # Nhận dữ liệu (Ví dụ: "Abc123@1,aF1#2w3E*,2We3345")
    data = conn.recv(1024).decode('utf-8')
    
    if data:
        # Cắt chuỗi thành danh sách các mật khẩu
        passwords = data.split(',')
        valid_passwords = []
        
        # Kiểm tra từng mật khẩu
        for p in passwords:
            if is_valid_password(p):
                valid_passwords.append(p)
        
        # Gom các mật khẩu hợp lệ lại thành 1 chuỗi, cách nhau bằng dấu phẩy
        result = ",".join(valid_passwords)
        
        # Nếu không có cái nào hợp lệ thì báo lỗi
        if not result:
            result = "Khong co mat khau nao hop le!"
            
        # Gửi kết quả về Client
        conn.send(result.encode('utf-8'))
        
    conn.close()