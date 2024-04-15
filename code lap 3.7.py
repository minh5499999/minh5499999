N = int(input("Nhập vào số nguyên dương N: "))

# Khởi tạo biến tổng S
tong_S = 0

# Tính tổng S
for i in range(1, N + 1):
    tong_S += i

# In kết quả
print("Tổng S là:", tong_S)