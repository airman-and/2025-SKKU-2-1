#include <iostream>
#include <string>
#include <vector>

// Base class with a virtual function
class Shape {
public:
    virtual void draw() {
        std::cout << "Drawing a generic shape." << std::endl;
    }
    virtual ~Shape() {} // Virtual destructor for proper cleanup
};

// Derived class Circle
class Circle : public Shape {
public:
    void draw() override {
        std::cout << "Drawing a circle." << std::endl;
    }
};

// Derived class Square
class Square : public Shape {
public:
    void draw() override {
        std::cout << "Drawing a square." << std::endl;
    }
};

// Derived class Triangle
class Triangle : public Shape {
public:
    void draw() override {
        std::cout << "Drawing a triangle." << std::endl;
    }
};

int main() {
    std::vector<Shape*> shapes;
    shapes.push_back(new Circle());
    shapes.push_back(new Square());
    shapes.push_back(new Triangle());
    shapes.push_back(new Shape());

    for (Shape* shape : shapes) {
        shape->draw(); // Calls the appropriate draw() method based on the object's actual type
    }

    // Clean up dynamically allocated memory
    for (Shape* shape : shapes) {
        delete shape;
    }
    shapes.clear();

    return 0;
}
