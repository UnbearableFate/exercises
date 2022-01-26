/*
 * @lc app=leetcode id=86 lang=cpp
 *
 * [86] Partition List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
//#include "../UsefulClasses.h"
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        if (head ==nullptr || head->next == nullptr) {
            return head;
        }
        ListNode* leftHead = nullptr;
        ListNode* leftTail = nullptr;
        ListNode* rightHead = nullptr;
        ListNode* rightTail = nullptr;
        for (ListNode *p = head; p != nullptr; p = p->next) {
            if (p->val < x) {
                if (leftHead == nullptr) {
                    leftHead = p;
                    leftTail = p;
                    continue;
                }
                leftTail->next = p;
                leftTail  = leftTail->next;
            } else {
                if (rightHead == nullptr) {
                    rightHead = p;
                    rightTail = p;
                    continue;
                }
                rightTail->next = p;
                rightTail = rightTail->next;
            }
        }
        if (leftHead == nullptr) {
            return rightHead;
        }
        if (rightHead == nullptr) {
            return leftHead;
        }
        leftTail->next = rightHead;
        rightTail->next = nullptr;
        return leftHead;
    }
};
// @lc code=end

int main() {
    ListNode* head = ListNode::createList({1,4,3,2,5,2});
    Solution a;
    cout << a.partition(head, 3) <<endl;
}