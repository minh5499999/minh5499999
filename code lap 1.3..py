import math

def tinh_dien_tich_hinh_vuong(e):
    dien_tich_hinh_vuong = e ** 2
    return dien_tich_hinh_vuong

def tinh_dien_tich_hinh_tron(r):
    dien_tich_hinh_tron = math.pi * r ** 2
    return dien_tich_hinh_tron

# Nhập giá trị cạnh hình vuông và bán kính hình tròn từ người dùng
e = float(input("Nhập giá trị cạnh của hình vuông: "))
r = float(input("Nhập giá trị bán kính của hình tròn: "))

# Gọi hàm tinh_dien_tich_hinh_vuong để tính diện tích hình vuông
dien_tich_hinh_vuong = tinh_dien_tich_hinh_vuong(e)

# Gọi hàm tinh_dien_tich_hinh_tron để tính diện tích hình tròn
dien_tich_hinh_tron = tinh_dien_tich_hinh_tron(r)

# So sánh diện tích và in ra kết quả
if dien_tich_hinh_vuong > dien_tich_hinh_tron:
    print("Diện tích hình vuông lớn hơn diện tích hình tròn.")
elif dien_tich_hinh_vuong < dien_tich_hinh_tron:
    print("Diện tích hình vuông nhỏ hơn diện tích hình tròn.")
else:
    print("Diện tích hình vuông bằng diện tích hình tròn.")