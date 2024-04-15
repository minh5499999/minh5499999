def nhanmatran(matran1, matran2):
    # Kiểm tra kích thước ma trận hợp lệ để nhân
    if len(matran1[0]) != len(matran2):
        return None

    # Khởi tạo ma trận kết quả
    hang = len(matran1)
    cot = len(matran2[0])
    matran_ketqua = [[0 for _ in range(cot)] for _ in range(hang)]

    # Nhân hai ma trận
    for i in range(hang):
        for j in range(cot):
            for k in range(len(matran2)):
                matran_ketqua[i][j] += matran1[i][k] * matran2[k][j]

    return matran_ketqua