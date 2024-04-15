def kiem_tra_chia_het(a, b):
    if a % b == 0:
        return True
    else:
        return False

# Nhập hai số nguyên dương từ người dùng
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))

# Kiểm tra xem a có chia hết cho b không
if kiem_tra_chia_het(a, b):
    print(a, "chia hết cho", b)
else:
    print(a, "không chia hết cho", b)