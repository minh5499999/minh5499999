def tim_ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def tim_bcnn(a, b):
    ucln = tim_ucln(a, b)
    bcnn = (a * b) // ucln
    return bcnn

# Nhập hai số nguyên dương từ người dùng
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))

# Tìm ước chung lớn nhất (UCLN)
ucln = tim_ucln(a, b)

# Tìm bội chung nhỏ nhất (BCNN)
bcnn = tim_bcnn(a, b)

# In kết quả
print("Ước chung lớn nhất (UCLN) của", a, "và", b, "là:", ucln)
print("Bội chung nhỏ nhất (BCNN) của", a, "và", b, "là:", bcnn)