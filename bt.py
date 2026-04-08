class PhanSo:
    def __init__(self, tu, mau=1):
        if mau == 0:
            raise ValueError("Mau so khong duoc bang 0")
        self.tu = tu
        self.mau = mau

    def __mul__(self, other):
        return PhanSo(self.tu * other.tu, self.mau * other.mau)

    def __truediv__(self, other):
        if other.tu == 0:
            raise ValueError("Khong the chia cho 0")
        return PhanSo(self.tu * other.mau, self.mau * other.tu)

    def __sub__(self, other):
        tu = self.tu * other.mau - other.tu * self.mau
        mau = self.mau * other.mau
        return PhanSo(tu, mau)

    def __str__(self):
        return f"{self.tu}/{self.mau}"


ps1 = PhanSo(2, 3)
ps2 = PhanSo(4, 5)

print(ps1)
print(ps2)
print("Hiệu:", ps1 - ps2)
print("Tích:", ps1 * ps2)
print("Thương:", ps1 / ps2)