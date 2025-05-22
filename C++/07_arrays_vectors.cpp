#include <iostream>
#include <vector>
#include <array>

int main() {
    // C-style array
    int arr[5] = {1, 2, 3, 4, 5};
    std::cout << "C-style array elements: ";
    for (int i = 0; i < 5; ++i) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;

    // std::array (fixed size)
    std::array<int, 5> std_arr = {6, 7, 8, 9, 10};
    std::cout << "std::array elements: ";
    for (int val : std_arr) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    // std::vector (dynamic size)
    std::vector<int> vec;
    vec.push_back(11);
    vec.push_back(12);
    vec.push_back(13);

    std::cout << "std::vector elements: ";
    for (int val : vec) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    vec.pop_back();
    std::cout << "std::vector after pop_back: ";
    for (int val : vec) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    std::cout << "Size of vector: " << vec.size() << std::endl;
    std::cout << "Capacity of vector: " << vec.capacity() << std::endl;

    return 0;
}
