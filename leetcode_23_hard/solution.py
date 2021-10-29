# Definition for singly-linked list.
from typing import List
import sys
import copy
from my_useful_methods import *

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def isListEmpty(lists):
    for node in lists :
        if node :
            return False
    return True

def findMin(lists) :
    minNode = [-1, sys.maxsize]
    for i in range(len(lists)):
        if lists[i] :
            if lists[i].val < minNode[1]:
                minNode = [i, lists[i].val]
    return minNode[0]

class Solution:
    def test(self, lists):
        lists.sort(key=lambda node: node.val)
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = ListNode()
        entryP = root

        while lists.count([]) > 0:
            lists.remove([])
        if len(lists) == 0:
            return None

        lists.sort(key=lambda node: node.val)
        while lists:
            minNode = copy.deepcopy(lists[0])
            lists = lists[1:]
            nodeWithoutHead = minNode.next
            entryP.next = ListNode()
            entryP.next.val = minNode.val
            entryP = entryP.next
            if nodeWithoutHead :
                pos = findPosListNode(nodeWithoutHead.val, lists, 0, len(lists))
                lists.insert(pos, nodeWithoutHead)

        return root

if __name__ == '__main__':
    a1 = ListNode(4,ListNode(4,ListNode(5)))
    a2 = ListNode(2, ListNode(3, ListNode(4)))
    a3 = ListNode(1,ListNode(6))
    li = [a1, a2, a3]
    ss = Solution()
    ww= ss.mergeKLists([[]])
    print(ww.val)