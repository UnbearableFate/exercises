/*
 * @lc app=leetcode id=232 lang=cpp
 *
 * [232] Implement Queue using Stacks
 */

// @lc code=start
#include<stack>
using namespace std;
class MyQueue {
private:
    stack<int> a;
    stack<int> b;
    void restore() {
        while (!b.empty())
        {
            a.push(b.top());
            b.pop();
        }
    }
public:
    MyQueue() {
    }
    
    void push(int x) {
       a.push(x); 
    }
    
    int pop() {
        while (a.size() > 1)
        {
            b.push(a.top());
            a.pop();
        }
        int res = a.top();
        a.pop();
        restore();
        return res;   
    }
    
    int peek() {
        while (a.size() > 1)
        {
            b.push(a.top());
            a.pop();
        }
        int res = a.top();
        restore();
        return res;
    }
    
    bool empty() {
       return a.empty(); 
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
// @lc code=end

