import math

def count_intersect_points(x1, y1, r1, x2, y2, r2):
    # Tính khoảng cách giữa hai tâm đường tròn
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # Kiểm tra trường hợp đường tròn nằm hoàn toàn trong nhau
    if distance <= abs(r1 - r2):
        return 0
    
    # Kiểm tra trường hợp đường tròn không cắt nhau
    if distance >= r1 + r2:
        return 0
    
    # Tính số điểm cắt nhau
    if distance < r1 + r2:
        # Tính hai giao điểm giữa hai đường tròn
        d = (r1**2 - r2**2 + distance**2) / (2 * distance)
        h = math.sqrt(r1**2 - d**2)
        
        # Tính tọa độ hai điểm cắt nhau
        x_intersect1 = x1 + (d * (x2 - x1)) / distance
        y_intersect1 = y1 + (d * (y2 - y1)) / distance
        x_intersect2 = x_intersect1 + (h * (y2 - y1)) / distance
        y_intersect2 = y_intersect1 - (h * (x2 - x1)) / distance
        
        # Kiểm tra nếu tọa độ hai điểm cắt nhau trùng nhau
        if x_intersect1 == x_intersect2 and y_intersect1 == y_intersect2:
            return 1
        else:
            return 2

# Nhập thông tin về đường tròn thứ nhất
x1 = float(input("Nhập tọa độ x của tâm đường tròn thứ nhất: "))
y1 = float(input("Nhập tọa độ y của tâm đường tròn thứ nhất: "))
r1 = float(input("Nhập bán kính đường tròn thứ nhất: "))

# Nhập thông tin về đường tròn thứ hai
x2 = float(input("Nhập tọa độ x của tâm đường tròn thứ hai: "))
y2 = float(input("Nhập tọa độ y của tâm đường tròn thứ hai: "))
r2 = float(input("Nhập bán kính đường tròn thứ hai: "))

# Tính số điểm cắt nhau
intersect_points = count_intersect_points(x1, y1, r1, x2, y2, r2)

# In kết quả
print("Số điểm mà hai đường tròn cắt nhau:", intersect_points)