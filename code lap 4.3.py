def tim_ky_tu(chuoi, i):
    # Kiểm tra tính hợp lệ của i nhập vào
    if i < 1 or i > len(chuoi):
        return '!'

    # Tìm ký tự xuất hiện i lần trong chuỗi
    for j in range(len(chuoi) - i + 1):
        ky_tu = chuoi[j]
        count = 1
        for k in range(j + 1, j + i):
            if chuoi[k] == ky_tu:
                count += 1

        if count == i:
            return ky_tu

    return '!'