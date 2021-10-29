#include<iostream>
#include<vector>
#include<queue>
#include <algorithm>
using namespace std;

struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 
class myGreater {
public:
    bool operator()(ListNode* a, ListNode* b) {
        return a->val > b->val;
    }
};

class Solution {
public:
    priority_queue <ListNode*,vector<ListNode*>, myGreater> qq;
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        auto res = new ListNode();
        ListNode *p = res;
        for (auto li : lists ) {
            qq.push(li);
        }
        while(!qq.empty()){
           p->next = qq.top();
           qq.pop();
           if (p->next->next != nullptr) {
               qq.push(p->next->next);
           }
           p->next->next = nullptr;
           p = p->next;
        }
        
        return res->next;
    }
};

int main() {
    auto ss = Solution();
    auto a1 = new ListNode(1,new ListNode(4,new ListNode(5)));
    auto a2 = new ListNode(1,new ListNode(3,new ListNode(4)));
    auto a3 = new ListNode(2,new ListNode(6));
    vector<ListNode *> bb = {a1, a2, a3};
    auto rr = ss.mergeKLists(bb);
    while(rr != nullptr) {
        cout<< rr->val <<endl;
        rr = rr->next;
    }
    return 0;
}
