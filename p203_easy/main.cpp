#include <iostream>
using namespace std;
class ListNode
{
    public:
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *removeElements(ListNode *head, int val)
    {
        ListNode headBeforehead = ListNode( -1, head);
        ListNode* p = &headBeforehead;
        while (p->next != nullptr)
        {
            if (p->next->val == val) {
                auto temp  = p->next;
                p->next = p->next->next;
                temp = nullptr;
                continue;
            }
            p = p->next;
        }
        return headBeforehead.next;
    }
};

int main()
{
    auto n1 = ListNode(4);
    auto n2 = ListNode(3, &n1);
    auto n0 = ListNode(1, &n2);
    auto ss = Solution();
    auto head = ss.removeElements(&n0,3);
    cout <<head->val<<endl;
    cout <<head->next->val <<endl;
    return 0;
}