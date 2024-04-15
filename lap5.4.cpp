#include <iostream>
using namespace std;

bool isPrime(int num) {
    if (num <= 1) {
        return false;
    }
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            return false;
        }
    }
    return true;
}

int sumPrimes(int n) {
    if (n <= 2) {
        return 0;
    }
    if (isPrime(n)) {
        return sumPrimes(n - 1) + n;
    } else {
        return sumPrimes(n - 1);
    }
}

int main() {
    int n;
    cout << "Enter a number: ";