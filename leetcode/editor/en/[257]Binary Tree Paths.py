# Given the root of a binary tree, return all root-to-leaf paths in any order. 
# 
#  A leaf is a node with no children. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1]
# Output: ["1"]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 100]. 
#  -100 <= Node.val <= 100 
#  
#  Related Topics String Backtracking Tree Depth-First Search Binary Tree 👍 399
# 2 👎 182


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Dict


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []
        stack = [root]
        sentence = dict()
        sentence[root.val] = str(root.val)
        result = []
        while len(stack) != 0:
            top = stack.pop()
            if top.left is None and top.right is None:
                result.append(sentence[top.val])
                continue
            if top.right is not None:
                sentence[top.right.val] = sentence[top.val] + "->" + str(top.right.val)
                stack.append(top.right)
            if top.left is not None:
                sentence[top.left.val] = sentence[top.val] + "->" + str(top.left.val)
                stack.append(top.left)
        return result
# leetcode submit region end(Prohibit modification and deletion)
