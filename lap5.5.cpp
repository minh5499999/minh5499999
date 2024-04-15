#include <iostream>
using namespace std;

int findMin(int a[], int n) {
    // Trường hợp cơ bản: Mảng chỉ có một phần tử
    if (n == 1) {
        return a[0];
    }
    
    // Tìm giá trị nhỏ nhất trong mảng con từ a[0] đến a[n-2]
    int minSubarray = findMin(a, n - 1);
    
    // So sánh giá trị nhỏ nhất của mảng con với a[n-1] để tìm giá trị nhỏ nhất của toàn bộ mảng
    if (a[n - 1] < minSubarray) {
        return a[n - 1];
    } else {
        return minSubarray;
    }
}

int main() {
    int n;
    cout << "Enter the size of the array: ";
    cin >> n;
    
    int* arr = new int[n];
    cout << "Enter the elements of the array: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    int minVal = findMin(arr, n);
    cout << "The minimum value in the array is: " << minVal << endl;
    
    delete[] arr;
    return 0;
}