#include <iostream>
#include <string>
#include <vector>

// Function template
template <typename T>
T add(T a, T b) {
    return a + b;
}

// Class template
template <typename T>
class Container {
private:
    T element;
public:
    Container(T elem) : element(elem) {}
    T getElement() const { return element; }
    void setElement(T elem) { element = elem; }
};

// Template specialization (optional, for specific types)
template <>
class Container<std::string> {
private:
    std::string element;
public:
    Container(std::string elem) : element(elem) {}
    std::string getElement() const { return element; }
    void setElement(std::string elem) { element = elem; }
    void printInfo() {
        std::cout << "This container holds a string: " << element << std::endl;
    }
};

int main() {
    // Using the function template
    std::cout << "add(5, 10): " << add(5, 10) << std::endl;
    std::cout << "add(3.14, 2.71): " << add(3.14, 2.71) << std::endl;
    std::cout << "add(std::string(\"Hello\"), std::string(\" World\")): " << add(std::string("Hello"), std::string(" World")) << std::endl;

    // Using the class template
    Container<int> intContainer(123);
    std::cout << "intContainer element: " << intContainer.getElement() << std::endl;

    Container<double> doubleContainer(45.67);
    std::cout << "doubleContainer element: " << doubleContainer.getElement() << std::endl;

    Container<std::string> stringContainer("Test String");
    std::cout << "stringContainer element: " << stringContainer.getElement() << std::endl;
    stringContainer.printInfo(); // Uses the specialized version

    return 0;
}
