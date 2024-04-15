#include <iostream>
using namespace std;

// Hàm sao chép dữ liệu từ mảng nguồn sang mảng đích
void copyArray(int* src, int* dest, int size) {
    for (int i = 0; i < size; i++) {
        if (*src % 2 == 0) {
            *dest = *src;
            dest++;
        }
        src++;
    }
}

int main() {
    int size;
    cout << "Nhập số phần tử của mảng nguồn: ";
    cin >> size;

    int* sourceArray = new int[size];
    int* destArray = new int[size];
    
    cout << "Nhập các phần tử của mảng nguồn: ";
    for (int i = 0; i < size; i++) {
        cin >> *(sourceArray + i);
    }

    copyArray(sourceArray, destArray, size);

    cout << "Mảng nguồn: ";
    for (int i = 0; i < size; i++) {
        cout << *(sourceArray + i) << " ";
    }

    cout << endl;

    cout << "Mảng đích (chứa các số chẵn): ";
    for (int i = 0; i < size; i++) {
        cout << *(destArray + i) << " ";
    }

    delete[] sourceArray;
    delete[] destArray;

    return 0;
}