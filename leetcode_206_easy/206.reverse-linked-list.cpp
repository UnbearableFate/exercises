/*
 * @lc app=leetcode id=206 lang=cpp
 *
 * [206] Reverse Linked List
 */

// @lc code=start
#include<stack>
using namespace std;
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        stack<ListNode*> nodeStack;
        while (head)
        {
            nodeStack.push(head);
            head = head->next;
        }
        if (nodeStack.empty()) {
            return nullptr;
        }
        auto res = nodeStack.top();
        auto p = res;
        nodeStack.pop();
        while (!nodeStack.empty())
        {
            p->next = nodeStack.top();
            p = p->next;
            nodeStack.pop();
        }
        p->next = nullptr;
        return res;
    }
};
// @lc code=end

int main() {
    ListNode *head = new ListNode(1,new ListNode(2,new ListNode(3)));
    Solution ss = Solution();
    auto res = ss.reverseList(head);
    cout <<res->val<<endl;
}