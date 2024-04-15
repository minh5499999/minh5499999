#include <iostream>
using namespace std;

// Hàm sao chép dữ liệu từ mảng nguồn sang mảng đích
void copyEvenNumbers(int* source, int* destination, int size) {
    int count = 0; // Biến đếm số lượng số chẵn được sao chép

    for (int i = 0; i < size; i++) {
        if (*source % 2 == 0) {
            *destination = *source;
            destination++;
            count++;
        }
        source++;
    }

    cout << "Số lượng số chẵn được sao chép: " << count << endl;
}

int main() {
    int size;
    cout << "Nhập số phần tử của mảng nguồn: ";
    cin >> size;

    int* sourceArray = new int[size];
    int* destinationArray = new int[size];

    cout << "Nhập các phần tử của mảng nguồn: ";
    for (int i = 0; i < size; i++) {
        cin >> *(sourceArray + i);
    }

    copyEvenNumbers(sourceArray, destinationArray, size);

    cout << "Mảng nguồn: ";
    for (int i = 0; i < size; i++) {
        cout << *(sourceArray + i) << " ";
    }

    cout << endl;

    cout << "Mảng đích (chứa các số chẵn): ";
    for (int i = 0; i < size; i++) {
        cout << *(destinationArray + i) << " ";
    }

    delete[] sourceArray;
    delete[] destinationArray;

    return 0;
}