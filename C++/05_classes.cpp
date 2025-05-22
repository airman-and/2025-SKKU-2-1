#include <iostream>
#include <string>

class Person {
public:
    std::string name;
    int age;

    void introduce() {
        std::cout << "Hello, my name is " << name << " and I am " << age << " years old." << std::endl;
    }
};

int main() {
    Person person1;
    person1.name = "Alice";
    person1.age = 25;
    person1.introduce();

    Person person2;
    person2.name = "Bob";
    person2.age = 32;
    person2.introduce();

    return 0;
}
