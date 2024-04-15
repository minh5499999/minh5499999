import math

def tinh_chu_vi(r):
    chu_vi = 2 * math.pi * r
    return chu_vi

# Nhập giá trị bán kính từ người dùng
r = float(input("Nhập giá trị bán kính của hình tròn: "))

# Gọi hàm tinh_chu_vi để tính chu vi
chu_vi = tinh_chu_vi(r)

# In ra kết quả
print("Chu vi của hình tròn là:", chu_vi)