#include<iostream>
#include<vector>
#include<set>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
 
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        set<ListNode*> nodeSet; 
        auto index = 1;
        while(headA != nullptr && headB != nullptr) {
            if(index > 0) {
                if(nodeSet.count(headA) > 0) {
                    return headA;
                }
                nodeSet.insert(headA);
                headA = headA->next;
            } else {
                if (nodeSet.count(headB) > 0){
                    return headB;
                }
                nodeSet.insert(headB);
                headB = headB->next;
            }
            index *= -1;
        }
        return nullptr;
    }
};
