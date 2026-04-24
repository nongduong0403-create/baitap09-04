import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

# --- 1. CẤU HÌNH MẠNG ---
IP = "127.0.0.1"
PORT = 8093

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(1)

client_conn = None

# Hàm chờ Client kết nối (chạy ngầm)
def accept_connection():
    global client_conn
    chat_area.insert(tk.END, f"[Hệ thống] Đang chờ kết nối tại Port {PORT}...\n")
    client_conn, addr = server.accept()
    chat_area.insert(tk.END, f"[Hệ thống] Đã kết nối với {addr}\n")
    
    # Bắt đầu luồng nhận tin nhắn liên tục
    threading.Thread(target=receive_messages, daemon=True).start()

# Hàm nhận tin nhắn từ Client (chạy ngầm)
def receive_messages():
    while True:
        try:
            data = client_conn.recv(1024).decode('utf-8')
            if data:
                chat_area.insert(tk.END, f"Client: {data}\n")
        except:
            chat_area.insert(tk.END, "[Hệ thống] Mất kết nối!\n")
            break

# Hàm gửi tin nhắn
def send_message(event=None):
    msg = msg_entry.get()
    if msg and client_conn:
        client_conn.send(msg.encode('utf-8'))
        chat_area.insert(tk.END, f"Server (Bạn): {msg}\n")
        msg_entry.delete(0, tk.END) # Xóa khung nhập sau khi gửi

# --- 2. CẤU HÌNH GIAO DIỆN (GUI) ---
root = tk.Tk()
root.title("Chat Server")

# Khung hiển thị tin nhắn
chat_area = scrolledtext.ScrolledText(root, width=45, height=15, state='normal')
chat_area.pack(padx=10, pady=10)

# Khung nhập tin nhắn
msg_entry = tk.Entry(root, width=35)
msg_entry.pack(side=tk.LEFT, padx=(10, 0), pady=10)
msg_entry.bind("<Return>", send_message) # Cho phép nhấn Enter để gửi

# Nút gửi
send_btn = tk.Button(root, text="Gửi", command=send_message)
send_btn.pack(side=tk.LEFT, padx=10, pady=10)

# Kích hoạt luồng chờ kết nối ở chế độ ngầm (daemon)
threading.Thread(target=accept_connection, daemon=True).start()

# Chạy vòng lặp giao diện
root.mainloop()