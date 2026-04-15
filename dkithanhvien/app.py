import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic

class AppDangKy(QDialog):
    def __init__(self):
        super(AppDangKy, self).__init__()
        
        # Đọc file thiết kế giao diện của bạn
        # LƯU Ý: Nếu file của bạn tên khác, hãy đổi chữ 'giaodien.ui' thành tên tương ứng
        uic.loadUi('giaodien.ui', self) 

# ==========================================
# KHỞI CHẠY ỨNG DỤNG
# ==========================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppDangKy()
    window.show()
    sys.exit(app.exec_())