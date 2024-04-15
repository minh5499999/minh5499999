#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

void init(int**& a, int m, int n) {
    a = new int*[m];
    for (int i = 0; i < m; i++) {
        a[i] = new int[n];
        for (int j = 0; j < n; j++) {
            a[i][j] = rand() % 10; // Khởi tạo giá trị ngẫu nhiên từ 0 đến 9
        }
    }
}

void transposeMatrix(int** a, int m, int n, int**& b) {
    b = new int*[n];
    for (int i = 0; i < n; i++) {
        b[i] = new int[m];
        for (int j = 0; j < m; j++) {
            b[i][j] = a[j][i]; // Lấy phần tử từ ma trận a và gán vào ma trận b theo quy tắc chuyển vị
        }
    }
}

void output(int** c, int m, int n) {
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cout << c[i][j] << " ";
        }
        cout << endl;
    }
}

void deleteMatrix(int** d, int m) {
    for (int i = 0; i < m; i++) {
        delete [] d[i];
    }
    delete [] d;
}

int main() {
    int m, n;
    int** a;
    int** b;
    cout << "Input the dimensions of the Matrix: ";
    cin >> m >> n;
    if (m <= 0 || n <= 0) {
        cout << "Invalid Input!" << endl;
    } else {
        init(a, m, n);
        cout << "The random matrix: " << endl;
        output(a, m, n);
        transposeMatrix(a, m, n, b);
        cout << "The transposing matrix: " << endl;
        output(b, n, m);
        deleteMatrix(a, m);
        deleteMatrix(b, n);
    }
    return 0;
}