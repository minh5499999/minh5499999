# Nhập hai số nguyên dương a và b
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))

# Kiểm tra xem a có chia hết cho b hay không
if a % b == 0:
    print(f"{a} chia hết cho {b}")
else:
    print(f"{a} không chia hết cho {b}")