/*
 * @lc app=leetcode id=234 lang=cpp
 *
 * [234] Palindrome Linked List
 */

// @lc code=start
// Definition for singly-linked list.
/*
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
*/
#include <vector>
#include <iostream>
using namespace std;
class Solution
{
public:
    bool isPalindrome(ListNode *head)
    {
        if (head->next == nullptr)
        {
            return true;
        }
        vector<int> left;
        ListNode *mid = head;
        ListNode *last = head->next;
        left.push_back(head->val);
        while (last->next != nullptr && last->next->next != nullptr)
        {
            mid = mid->next;
            left.push_back(mid->val);
            last = last->next->next;
        }

        if (last->next != nullptr)
        {
            mid = mid->next;
        }

        for (int j = left.size() - 1; j >= 0; --j)
        {
            if (left[j] == mid->next->val)
            {
                mid = mid->next;
            }
            else
            {
                return false;
            }
        }
        return true;
    }
};
// @lc code=end

int main() {
    ListNode *head = new ListNode(1,new ListNode(2,new ListNode(2, new ListNode(3))));
    Solution cc;
    cout << cc.isPalindrome(head) <<endl;
    return 0;
}