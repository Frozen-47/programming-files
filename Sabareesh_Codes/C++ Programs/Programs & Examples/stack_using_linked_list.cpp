// C++ Program: Stack using Linked List
// Date: 2026-08-30

#include <iostream>

using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

class LinkedListStack {
private:
    Node* top;
public:
    LinkedListStack() : top(nullptr) {}

    void push(int val) {
        Node* newNode = new Node(val);
        newNode->next = top;
        top = newNode;
    }

    int pop() {
        if (!top) {
            cout << "Stack Underflow\n";
            return -1;
        }
        int val = top->data;
        Node* temp = top;
        top = top->next;
        delete temp;
        return val;
    }

    bool isEmpty() const {
        return top == nullptr;
    }
};

int main() {
    LinkedListStack s;
    s.push(100);
    s.push(200);
    s.push(300);
    cout << "Popped: " << s.pop() << endl;
    cout << "Popped: " << s.pop() << endl;
    return 0;
}
