def tinh_giai_thua(n):
    giai_thua = 1
    if n < 0:
        return "Không thể tính giai thừa cho số âm."
    elif n == 0:
        return giai_thua
    else:
        for i in range(1, n + 1):
            giai_thua *= i
        return giai_thua

# Nhập giá trị N từ người dùng
N = int(input("Nhập giá trị N: "))

# Gọi hàm tinh_giai_thua để tính giai thừa
ket_qua = tinh_giai_thua(N)

# In ra kết quả
print("Giai thừa của", N, "là:", ket_qua)