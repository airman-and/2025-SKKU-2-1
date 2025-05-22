#include <iostream>

// Function declaration
int add(int a, int b);

int main() {
    int num1 = 5;
    int num2 = 10;
    int sum = add(num1, num2);

    std::cout << "The sum of " << num1 << " and " << num2 << " is " << sum << std::endl;

    return 0;
}

// Function definition
int add(int a, int b) {
    return a + b;
}
