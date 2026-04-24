import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

# --- 1. CẤU HÌNH MẠNG ---
SERVER_IP = "127.0.0.1"
SERVER_PORT = 8093

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Hàm nhận tin nhắn từ Server (chạy ngầm)
def receive_messages():
    while True:
        try:
            data = client.recv(1024).decode('utf-8')
            if data:
                chat_area.insert(tk.END, f"Server: {data}\n")
        except:
            chat_area.insert(tk.END, "[Hệ thống] Mất kết nối tới Server!\n")
            break

# Hàm gửi tin nhắn
def send_message(event=None):
    msg = msg_entry.get()
    if msg:
        try:
            client.send(msg.encode('utf-8'))
            chat_area.insert(tk.END, f"Client (Bạn): {msg}\n")
            msg_entry.delete(0, tk.END)
        except:
            chat_area.insert(tk.END, "[Hệ thống] Lỗi gửi tin nhắn!\n")

# --- 2. CẤU HÌNH GIAO DIỆN (GUI) ---
root = tk.Tk()
root.title("Chat Client")

chat_area = scrolledtext.ScrolledText(root, width=45, height=15)
chat_area.pack(padx=10, pady=10)

msg_entry = tk.Entry(root, width=35)
msg_entry.pack(side=tk.LEFT, padx=(10, 0), pady=10)
msg_entry.bind("<Return>", send_message)

send_btn = tk.Button(root, text="Gửi", command=send_message)
send_btn.pack(side=tk.LEFT, padx=10, pady=10)

# Thực hiện kết nối tới Server trước khi mở giao diện
try:
    client.connect((SERVER_IP, SERVER_PORT))
    chat_area.insert(tk.END, f"[Hệ thống] Đã kết nối tới Server {SERVER_IP}:{SERVER_PORT}\n")
    
    # Kích hoạt luồng nhận tin nhắn
    threading.Thread(target=receive_messages, daemon=True).start()
except:
    chat_area.insert(tk.END, "[Hệ thống] Không thể kết nối đến Server! Hãy chắc chắn Server đang chạy.\n")

# Chạy vòng lặp giao diện
root.mainloop()