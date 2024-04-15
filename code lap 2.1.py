def kiem_tra_ket_qua(player1, player2):
    if player1 == player2:
        return "Hòa"
    elif (player1 == "búa" and player2 == "bao") or (player1 == "bao" and player2 == "kéo") or (player1 == "kéo" and player2 == "búa") or (player1 == "kéo" and player2 == "bao"):
        return "Người chơi 1 thắng"
    else:
        return "Người chơi 2 thắng"

# Nhập lựa chọn của hai người chơi từ người dùng
player1 = input("Người chơi 1 - Nhập lựa chọn (kéo/búa/bao): ").lower()
player2 = input("Người chơi 2 - Nhập lựa chọn (kéo/búa/bao): ").lower()

# Kiểm tra kết quả trò chơi
ket_qua = kiem_tra_ket_qua(player1, player2)

# In kết quả
print("Kết quả:", ket_qua)