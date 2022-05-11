# Given the head of a singly linked list where elements are sorted in ascending 
# order, convert it to a height balanced BST. 
# 
#  For this problem, a height-balanced binary tree is defined as a binary tree 
# in which the depth of the two subtrees of every node never differ by more than 1.
#  
# 
#  
#  Example 1: 
# 
#  
# Input: head = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the 
# shown height balanced BST.
#  
# 
#  Example 2: 
# 
#  
# Input: head = []
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in head is in the range [0, 2 * 10⁴]. 
#  -10⁵ <= Node.val <= 10⁵ 
#  
#  Related Topics Linked List Divide and Conquer Tree Binary Search Tree Binary 
# Tree 👍 4508 👎 113
from typing import Optional

from leetcode.editor.en.UsefulClass import TreeNode
from leetcode.editor.en.UsefulClass import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:
            return None
        length = 0
        p = head
        while p is not None:
            length += 1
            p = p.next
        if length == 1 :
            return TreeNode(head.val)
        midIndex = int(length / 2)
        pNode = head
        for i in range(0,midIndex-1):
            pNode = pNode.next
        midNode = pNode.next
        pNode.next = None

        root = TreeNode(midNode.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(midNode.next)

        return root

# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    head = ListNode(-10,ListNode(-3,ListNode(0,ListNode(5, ListNode(9)))))
    print(s.sortedListToBST(head))