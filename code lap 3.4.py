def tim_USCLN(a, b):
    while(b):
        a, b = b, a % b
    return a

def kiem_tra_nguyen_to_cung_nhau(m, n):
    if tim_USCLN(m, n) == 1:
        return True
    else:
        return False

m = int(input("Nhập số nguyên dương m: "))
n = int(input("Nhập số nguyên dương n: "))

if kiem_tra_nguyen_to_cung_nhau(m, n):
    print(f"{m} và {n} là hai số nguyên tố cùng nhau.")
else:
    print(f"{m} và {n} không là hai số nguyên tố cùng nhau.")