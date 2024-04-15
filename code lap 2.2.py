import math

def solve_quadratic_equation(a, b, c):
    # Tính delta
    delta = b**2 - 4*a*c
    
    if delta > 0:  # Phương trình có 2 nghiệm thực phân biệt
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2
    elif delta == 0:  # Phương trình có nghiệm kép
        x = -b / (2*a)
        return x
    else:  # Phương trình không có nghiệm thực
        return None

# Nhập các hệ số a, b, c
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# Giải phương trình
solutions = solve_quadratic_equation(a, b, c)

# Kiểm tra số lượng nghiệm
if solutions is None:
    print("Phương trình không có nghiệm thực.")
elif isinstance(solutions, tuple):
    print("Phương trình có 2 nghiệm:")
    print("x1 =", solutions[0])
    print("x2 =", solutions[1])
else:
    print("Phương trình có nghiệm kép:")
    print("x =", solutions)