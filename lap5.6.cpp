#include <iostream>
using namespace std;

int sumEvenDigit(int n) {
    if (n < 0) {
        return -1;
    }
    if (n == 0) {
        return 0;
    }
    int lastDigit = n % 10;
    if (lastDigit % 2 == 0) {
        return sumEvenDigit(n / 10);
    } else {
        return lastDigit + sumEvenDigit(n / 10);
    }
}

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;
    int sum = sumEvenDigit(n);
    cout << "Sum of odd digits of " << n << ": " << sum << endl;
    return 0;
}