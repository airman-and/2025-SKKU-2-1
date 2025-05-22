#include <iostream>
#include <stdexcept> // For standard exceptions like std::out_of_range
#include <vector>

// Function that might throw an exception
double divide(double numerator, double denominator) {
    if (denominator == 0) {
        throw std::runtime_error("Division by zero error!");
    }
    return numerator / denominator;
}

// Custom exception class
class MyCustomException : public std::exception {
public:
    const char* what() const noexcept override {
        return "My custom exception occurred!";
    }
};

void processVector(const std::vector<int>& vec, int index) {
    if (index < 0 || index >= vec.size()) {
        throw std::out_of_range("Vector index out of range!");
    }
    std::cout << "Element at index " << index << " is " << vec.at(index) << std::endl;
}

int main() {
    // Example 1: Handling division by zero
    try {
        double result = divide(10.0, 2.0);
        std::cout << "10.0 / 2.0 = " << result << std::endl;

        result = divide(5.0, 0.0); // This will throw an exception
        std::cout << "This line will not be printed." << std::endl;
    } catch (const std::runtime_error& e) {
        std::cerr << "Caught a runtime_error: " << e.what() << std::endl;
    }

    std::cout << "\n--- Example 2: Handling vector out of range --- " << std::endl;
    std::vector<int> numbers = {10, 20, 30};
    try {
        processVector(numbers, 1);  // Valid index
        processVector(numbers, 5);  // Invalid index, will throw
    } catch (const std::out_of_range& e) {
        std::cerr << "Caught an out_of_range error: " << e.what() << std::endl;
    }

    std::cout << "\n--- Example 3: Handling custom exception --- " << std::endl;
    try {
        // Simulate a condition for custom exception
        bool errorCondition = true;
        if (errorCondition) {
            throw MyCustomException();
        }
    } catch (const MyCustomException& e) {
        std::cerr << "Caught MyCustomException: " << e.what() << std::endl;
    } catch (const std::exception& e) { // Catch any other standard exceptions
        std::cerr << "Caught a standard exception: " << e.what() << std::endl;
    }

    std::cout << "\nProgram continues after handling exceptions." << std::endl;
    return 0;
}
