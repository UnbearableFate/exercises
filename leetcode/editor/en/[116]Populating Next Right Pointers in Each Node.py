# You are given a perfect binary tree where all leaves are on the same level, 
# and every parent has two children. The binary tree has the following definition: 
# 
#  
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
#  
# 
#  Populate each next pointer to point to its next right node. If there is no 
# next right node, the next pointer should be set to NULL. 
# 
#  Initially, all next pointers are set to NULL. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), your function 
# should populate each next pointer to point to its next right node, just like in 
# Figure B. The serialized output is in level order as connected by the next 
# pointers, with '#' signifying the end of each level.
#  
# 
#  Example 2: 
# 
#  
# Input: root = []
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 2¹² - 1]. 
#  -1000 <= Node.val <= 1000 
#  
# 
#  
#  Follow-up: 
# 
#  
#  You may only use constant extra space. 
#  The recursive approach is fine. You may assume implicit stack space does not 
# count as extra space for this problem. 
#  
#  Related Topics Linked List Tree Depth-First Search Breadth-First Search 
# Binary Tree 👍 6353 👎 230
import math

from UsefulClass import Node
from typing import Optional

# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:

    def judge(self,num):
        num = int(num)
        return True if num == 0 or num & (num - 1) == 0 else False

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        queue = [root]
        index = 0
        while len(queue) > 0:
            top = queue.pop(0)
            index += 1
            if not self.judge(index+1):
                top.next = queue[0]
            if top.left is not None:
                queue.append(top.left)
            if top.right is not None:
                queue.append(top.right)

        return root

# leetcode submit region end(Prohibit modification and deletion)
