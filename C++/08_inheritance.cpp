#include <iostream>
#include <string>

// Base class
class Animal {
public:
    std::string name;

    Animal(std::string n) : name(n) {}

    void eat() {
        std::cout << name << " is eating." << std::endl;
    }

    void sleep() {
        std::cout << name << " is sleeping." << std::endl;
    }
};

// Derived class
class Dog : public Animal {
public:
    Dog(std::string n) : Animal(n) {}

    void bark() {
        std::cout << name << " is barking." << std::endl;
    }
};

// Another derived class
class Cat : public Animal {
public:
    Cat(std::string n) : Animal(n) {}

    void meow() {
        std::cout << name << " is meowing." << std::endl;
    }
};

int main() {
    Dog myDog("Buddy");
    myDog.eat();
    myDog.sleep();
    myDog.bark();

    Cat myCat("Whiskers");
    myCat.eat();
    myCat.sleep();
    myCat.meow();

    return 0;
}
