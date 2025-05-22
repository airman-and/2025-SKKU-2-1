#include <iostream>

int main() {
    int var = 10;
    int *ptr = &var;

    std::cout << "Value of var: " << var << std::endl;
    std::cout << "Address of var: " << &var << std::endl;
    std::cout << "Value of ptr: " << ptr << std::endl;
    std::cout << "Value pointed to by ptr: " << *ptr << std::endl;

    *ptr = 20; // Modify the value using the pointer
    std::cout << "New value of var: " << var << std::endl;

    // Dynamic memory allocation
    int *dynamic_ptr = new int;
    *dynamic_ptr = 30;
    std::cout << "Value of dynamically allocated memory: " << *dynamic_ptr << std::endl;
    delete dynamic_ptr; // Deallocate memory

    return 0;
}
