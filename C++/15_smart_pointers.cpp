#include <iostream>
#include <memory> // Required for smart pointers
#include <string>
#include <vector>

class MyResource {
public:
    int id;
    MyResource(int i) : id(i) {
        std::cout << "MyResource " << id << " created." << std::endl;
    }
    ~MyResource() {
        std::cout << "MyResource " << id << " destroyed." << std::endl;
    }
    void print() const {
        std::cout << "MyResource ID: " << id << std::endl;
    }
};

void process_unique_ptr(std::unique_ptr<MyResource> ptr) {
    if (ptr) {
        std::cout << "Processing unique_ptr in function: ";
        ptr->print();
    } else {
        std::cout << "unique_ptr is null in function." << std::endl;
    }
    // ptr goes out of scope here, and the resource is deallocated if ptr owns it
}

void observe_shared_ptr(std::shared_ptr<MyResource> s_ptr) {
    std::cout << "Observing shared_ptr (use count: " << s_ptr.use_count() << "): ";
    if (s_ptr) {
        s_ptr->print();
    }
    // s_ptr goes out of scope, use count decreases
}

void observe_weak_ptr(std::weak_ptr<MyResource> w_ptr) {
    std::cout << "Observing weak_ptr: ";
    if (auto locked_ptr = w_ptr.lock()) { // Try to acquire a shared_ptr
        std::cout << "Resource is alive (use count: " << locked_ptr.use_count() << "): ";
        locked_ptr->print();
    } else {
        std::cout << "Resource is no longer alive." << std::endl;
    }
}

int main() {
    // 1. std::unique_ptr: Exclusive ownership
    std::cout << "--- std::unique_ptr Example --- " << std::endl;
    {
        std::unique_ptr<MyResource> u_ptr1(new MyResource(1));
        if (u_ptr1) {
            u_ptr1->print();
        }

        // Ownership transfer (u_ptr1 becomes null)
        std::unique_ptr<MyResource> u_ptr2 = std::move(u_ptr1);
        if (u_ptr2) {
            std::cout << "u_ptr2: ";
            u_ptr2->print();
        }
        if (!u_ptr1) {
            std::cout << "u_ptr1 is now null after move." << std::endl;
        }

        // Pass to function (ownership is moved)
        process_unique_ptr(std::move(u_ptr2)); 
        // u_ptr2 is now null here, resource managed by function scope
        if (!u_ptr2) {
            std::cout << "u_ptr2 is null after being passed to function." << std::endl;
        }

        // Using std::make_unique (C++14 and later, preferred)
        std::unique_ptr<MyResource> u_ptr3 = std::make_unique<MyResource>(2);
        u_ptr3->print();
    } // u_ptr3 goes out of scope, MyResource(2) is destroyed
    std::cout << std::endl;

    // 2. std::shared_ptr: Shared ownership (reference counting)
    std::cout << "--- std::shared_ptr Example --- " << std::endl;
    std::shared_ptr<MyResource> s_ptr1;
    {
        s_ptr1 = std::make_shared<MyResource>(3); // Preferred way to create shared_ptr
        std::cout << "s_ptr1 use count: " << s_ptr1.use_count() << std::endl; // Should be 1

        {
            std::shared_ptr<MyResource> s_ptr2 = s_ptr1; // Copying increases use count
            std::cout << "s_ptr1 use count: " << s_ptr1.use_count() << std::endl; // Should be 2
            std::cout << "s_ptr2 use count: " << s_ptr2.use_count() << std::endl; // Should be 2
            s_ptr2->print();
        } // s_ptr2 goes out of scope, use count decreases

        std::cout << "s_ptr1 use count after s_ptr2 scope: " << s_ptr1.use_count() << std::endl; // Should be 1
        observe_shared_ptr(s_ptr1); // Pass by value, use count increases temporarily
        std::cout << "s_ptr1 use count after observe_shared_ptr: " << s_ptr1.use_count() << std::endl; // Should be 1
    } // s_ptr1 goes out of scope, MyResource(3) is destroyed as use count becomes 0
    std::cout << std::endl;

    // 3. std::weak_ptr: Non-owning observer of a std::shared_ptr
    // Useful for breaking circular dependencies
    std::cout << "--- std::weak_ptr Example --- " << std::endl;
    std::weak_ptr<MyResource> w_ptr1;
    {
        auto s_ptr_for_weak = std::make_shared<MyResource>(4);
        w_ptr1 = s_ptr_for_weak; // w_ptr1 observes s_ptr_for_weak

        observe_weak_ptr(w_ptr1);
        std::cout << "s_ptr_for_weak use count: " << s_ptr_for_weak.use_count() << std::endl; // Should be 1

    } // s_ptr_for_weak goes out of scope, MyResource(4) is destroyed
    
    observe_weak_ptr(w_ptr1); // Now the resource should be gone

    std::cout << "\nProgram finished." << std::endl;
    return 0;
}
