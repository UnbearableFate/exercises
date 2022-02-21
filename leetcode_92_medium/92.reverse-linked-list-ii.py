#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        stack =[]
        parent = ListNode(-1,head)
        for i in range(0,left-1):
            parent = parent.next
        p = parent.next
        for i in range(left, right):
            stack.append(p)
            p = p.next
        son = p.next
        while len(stack) > 0:
            k = stack.pop()
            parent.next = k
            parent = parent.next
        parent.next = son
        return head
# @lc code=end

if __name__ == "__main__" :
    ss = Solution()
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    print(ss.reverseBetween())