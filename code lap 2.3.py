def swap_without_temp(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

# Nhập hai số nguyên dương
num1 = int(input("Nhập số nguyên dương thứ nhất: "))
num2 = int(input("Nhập số nguyên dương thứ hai: "))

# Hoán vị
num1, num2 = swap_without_temp(num1, num2)

# In kết quả
print("Sau khi hoán vị:")
print("Số nguyên dương thứ nhất =", num1)
print("Số nguyên dương thứ hai =", num2)