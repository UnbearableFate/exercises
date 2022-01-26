/*
 * @lc app=leetcode id=82 lang=cpp
 *
 * [82] Remove Duplicates from Sorted List II
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
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* p= new ListNode(0,head);
        ListNode* res = p;
        while (p!= nullptr && p->next != nullptr && p->next->next != nullptr)
        {
            if (p->next->val != p->next->next->val) {
                p = p->next;
                continue;
            } else {
                int v = p->next->val;
                while (p->next != nullptr && p->next->val == v)
                {
                    p->next = p->next->next;
                }
            }
        }
        return res->next;
    }
};
// @lc code=end

