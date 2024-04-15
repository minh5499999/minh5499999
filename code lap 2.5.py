from datetime import date

# Ngày hiện tại
current_date = date(1999, 12, 31)

# Nhập ngày sinh
year_of_birth = int(input("Nhập năm sinh (1901-1999): "))
month_of_birth = int(input("Nhập tháng sinh (1-12): "))
day_of_birth = int(input("Nhập ngày sinh (1-31): "))

# Ngày sinh
birth_date = date(year_of_birth, month_of_birth, day_of_birth)

# Tính số lần sinh nhật
num_birthdays = current_date.year - birth_date.year

# Kiểm tra nếu chưa đến ngày sinh nhật trong năm nay
if (birth_date.month, birth_date.day) > (current_date.month, current_date.day):
    num_birthdays -= 1

# In kết quả
print("Số lần sinh nhật từ ngày sinh đến ngày hiện tại:", num_birthdays)