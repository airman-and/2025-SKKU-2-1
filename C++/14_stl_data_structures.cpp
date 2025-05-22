#include <iostream>
#include <vector>
#include <string>
#include <map>      // For std::map
#include <set>      // For std::set
#include <unordered_map> // For std::unordered_map
#include <unordered_set> // For std::unordered_set
#include <list>     // For std::list
#include <deque>    // For std::deque
#include <stack>    // For std::stack
#include <queue>    // For std::queue

int main() {
    // 1. std::vector (Dynamic Array) - already covered, but good to reiterate
    std::vector<int> vec = {1, 2, 3, 4, 5};
    vec.push_back(6);
    std::cout << "Vector: ";
    for (int v : vec) std::cout << v << " ";
    std::cout << std::endl;

    // 2. std::list (Doubly Linked List)
    std::list<std::string> strList = {"apple", "banana"};
    strList.push_front("orange");
    strList.push_back("grape");
    std::cout << "List: ";
    for (const auto& s : strList) std::cout << s << " ";
    std::cout << std::endl;

    // 3. std::deque (Double-Ended Queue)
    std::deque<int> deq = {10, 20, 30};
    deq.push_front(5);
    deq.push_back(35);
    std::cout << "Deque: ";
    for (int d : deq) std::cout << d << " ";
    std::cout << std::endl;

    // 4. std::map (Ordered Key-Value Store - Red-Black Tree)
    std::map<std::string, int> ages;
    ages["Alice"] = 30;
    ages["Bob"] = 25;
    ages.insert({"Charlie", 35});
    std::cout << "Map (ages):\n";
    for (const auto& pair : ages) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }
    std::cout << "Bob's age: " << ages["Bob"] << std::endl;

    // 5. std::unordered_map (Unordered Key-Value Store - Hash Table)
    std::unordered_map<std::string, double> prices;
    prices["milk"] = 2.50;
    prices["bread"] = 1.75;
    prices.insert({"eggs", 3.00});
    std::cout << "Unordered Map (prices):\n";
    for (const auto& pair : prices) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }

    // 6. std::set (Ordered Unique Elements - Red-Black Tree)
    std::set<int> unique_numbers = {5, 2, 8, 2, 5, 1};
    unique_numbers.insert(10);
    std::cout << "Set (unique numbers): ";
    for (int n : unique_numbers) std::cout << n << " "; // Will be sorted: 1 2 5 8 10
    std::cout << std::endl;

    // 7. std::unordered_set (Unordered Unique Elements - Hash Table)
    std::unordered_set<std::string> tags = {"c++", "programming", "code", "c++"};
    tags.insert("stl");
    std::cout << "Unordered Set (tags): ";
    for (const auto& tag : tags) std::cout << tag << " ";
    std::cout << std::endl;

    // 8. std::stack (LIFO Adapter - uses deque by default)
    std::stack<int> myStack;
    myStack.push(100);
    myStack.push(200);
    myStack.push(300);
    std::cout << "Stack (top to bottom): ";
    while(!myStack.empty()) {
        std::cout << myStack.top() << " ";
        myStack.pop();
    }
    std::cout << std::endl;

    // 9. std::queue (FIFO Adapter - uses deque by default)
    std::queue<std::string> myQueue;
    myQueue.push("First");
    myQueue.push("Second");
    myQueue.push("Third");
    std::cout << "Queue (front to back): ";
    while(!myQueue.empty()) {
        std::cout << myQueue.front() << " ";
        myQueue.pop();
    }
    std::cout << std::endl;

    // 10. std::priority_queue (Heap - largest element has highest priority by default)
    std::priority_queue<int> pq;
    pq.push(30); pq.push(100); pq.push(20); pq.push(80);
    std::cout << "Priority Queue (max heap): ";
    while(!pq.empty()) {
        std::cout << pq.top() << " "; // Accesses the largest element
        pq.pop();
    }
    std::cout << std::endl;

    // Priority queue with custom comparator (min heap)
    std::priority_queue<int, std::vector<int>, std::greater<int>> min_pq;
    min_pq.push(30); min_pq.push(100); min_pq.push(20); min_pq.push(80);
    std::cout << "Priority Queue (min heap): ";
    while(!min_pq.empty()) {
        std::cout << min_pq.top() << " "; // Accesses the smallest element
        min_pq.pop();
    }
    std::cout << std::endl;

    return 0;
}
