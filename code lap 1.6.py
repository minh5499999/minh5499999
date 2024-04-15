def tim_gia_tri_lon_nhat(arr):
    max_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value

def tim_gia_tri_nho_nhat(arr):
    min_value = arr[0]
    for num in arr:
        if num < min_value:
            min_value = num
    return min_value

# Nhập số lượng phần tử của mảng từ người dùng
N = int(input("Nhập số lượng phần tử của mảng: "))

# Khởi tạo mảng và nhập giá trị từ người dùng
arr = []
for i in range(N):
    num = int(input("Nhập phần tử thứ {}:".format(i+1)))
    arr.append(num)

# Tìm giá trị lớn nhất
max_value = tim_gia_tri_lon_nhat(arr)

# Tìm giá trị nhỏ nhất
min_value = tim_gia_tri_nho_nhat(arr)

# In kết quả
print("Giá trị lớn nhất trong mảng là:", max_value)
print("Giá trị nhỏ nhất trong mảng là:", min_value)