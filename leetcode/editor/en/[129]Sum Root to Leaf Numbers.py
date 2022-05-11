# You are given the root of a binary tree containing digits from 0 to 9 only. 
# 
#  Each root-to-leaf path in the tree represents a number. 
# 
#  
#  For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123. 
#  
# 
#  Return the total sum of all root-to-leaf numbers. Test cases are generated 
# so that the answer will fit in a 32-bit integer. 
# 
#  A leaf node is a node with no children. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,2,3]
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
#  
# 
#  Example 2: 
# 
#  
# Input: root = [4,9,0,5,1]
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 1000]. 
#  0 <= Node.val <= 9 
#  The depth of the tree will not exceed 10. 
#  
#  Related Topics Tree Depth-First Search Binary Tree 👍 4181 👎 80



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from leetcode.editor.en.UsefulClass import TreeNode

# leetcode submit region begin(Prohibit modification and deletion)
class MyNode:
    def __init__(self, node, parent):
        self.node = node
        self.parent = parent
        if parent:
            self.number = self.parent.number * 10 + self.node.val
        else:
            self.number = self.node.val
        self.color = 0


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        routes = []
        stack = [MyNode(root, None)]
        while len(stack) > 0:
            top = stack[-1]
            if top.color == 0:
                if top.node.left is not None:
                    stack.append(MyNode(top.node.left, top))
                if top.node.right is not None:
                    stack.append(MyNode(top.node.right, top))
                top.color = 1
                continue
            else:
                top = stack.pop()
                if top.node.left is None and top.node.right is None:
                    routes.append(top.number)
        return sum(routes)

# leetcode submit region end(Prohibit modification and deletion)
