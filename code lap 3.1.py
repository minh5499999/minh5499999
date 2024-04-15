def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Nhập số nguyên từ người dùng
n = int(input("Nhập số nguyên: "))

# Kiểm tra xem n có phải là số nguyên tố hay không
if is_prime(n):
    print(n, "là số nguyên tố")
else:
    print(n, "không là số nguyên tố")