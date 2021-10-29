# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def reversedList(head: ListNode, n :int) :
    if not head :
        return None, None
    p = head
    pNext = head.next
    if pNext :
        p.next = None
    index = 1
    while pNext and index < n:
        tempNext = pNext.next
        pNext.next = p
        p = pNext
        pNext = tempNext
        index += 1
    return p, head , pNext

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        reHead, reTail, reNextHead = reversedList(head, k)
        result = reHead
        while reNextHead:
            reHead, reTail, reNextHead = reversedList(reHead, k)
            if reNextHead :
                reTail.next = reversedList(reNextHead,k)
            else :
                break
        return result

if __name__ == '__main__':
    li = ListNode(1,ListNode(2, ListNode(3,ListNode(4))))
    ss = Solution()
    ww = ss.reverseKGroup(li, 2)
