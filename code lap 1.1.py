def tinh_tong(a, b, c):
    tong = a + b + c
    return tong

# Nhập các giá trị của a, b và c từ người dùng
a = int(input("Nhập giá trị của a: "))
b = int(input("Nhập giá trị của b: "))
c = int(input("Nhập giá trị của c: "))

# Gọi hàm tinh_tong để tính tổng của a, b và c
tong = tinh_tong(a, b, c)

# In ra kết quả
print("Tổng của ba số nguyên a, b và c là:", tong)
