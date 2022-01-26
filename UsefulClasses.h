#include<initializer_list>
#include<iostream>
using namespace std;
struct ListNode
{
	int val;
	ListNode *next;
	ListNode() : val(0), next(nullptr) {}
	ListNode(int x) : val(x), next(nullptr) {}
	ListNode(int x, ListNode *next) : val(x), next(next) {}
	static ListNode* createList(std::initializer_list<int> li) {
		ListNode *head = new ListNode(*li.begin());
		auto p = head;
		for(auto i = li.begin()+1; i != li.end();++i) {
			p->next = new ListNode(*i);
			p = p->next;
		}
		return head;
	}
};