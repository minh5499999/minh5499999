N = int(input("Nhập vào số nguyên dương N: "))

# Khởi tạo biến tổng ước số
tong_uoc_so = 0

# Duyệt qua các số từ 2 đến N//2
for i in range(2, N//2 + 1):
    if N % i == 0:
        tong_uoc_so += i

# In kết quả
print("Tổng các ước số của", N, "là:", tong_uoc_so)