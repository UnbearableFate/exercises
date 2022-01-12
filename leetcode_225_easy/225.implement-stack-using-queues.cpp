/*
 * @lc app=leetcode id=225 lang=cpp
 *
 * [225] Implement Stack using Queues
 */

// @lc code=start
#include<queue>
#include<iostream>
using namespace std;
class MyStack {
private:
    queue<int> q1;
    queue<int> q2;
    int t;
public:
    MyStack() {
        
    }
    
    void push(int x) {
        q1.push(x);
        t = x;
    }
    
    int pop() {
        while(!q2.empty()) {
            q2.pop();
        }
        int size = q1.size() -1;
        for (size_t i = 0; i < size; i++)
        {
            q2.push(q1.front());
            t = q1.front();
            q1.pop();
        }
        q1.swap(q2);

        return q2.front();
    }
    
    int top() {
        return t;
    }
    
    bool empty() {
        return q1.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */
// @lc code=end

int main() {
    MyStack s;
    s.push(1);
    s.push(2);
    s.push(3);
    cout << s.top() << endl;
    cout << s.pop() << endl;
    cout << s.pop() << endl;
    cout << s.pop() << endl;
    cout << s.empty() << endl;
}