# Given an integer n, return all the structurally unique BST's (binary search 
# trees), which has exactly n nodes of unique values from 1 to n. Return the answer 
# in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 3
# Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]
# ]
#  
# 
#  Example 2: 
# 
#  
# Input: n = 1
# Output: [[1]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 8 
#  
#  Related Topics Dynamic Programming Backtracking Tree Binary Search Tree 
# Binary Tree 👍 4453 👎 292


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def createTree(self,parent :TreeNode,beg:int, end:int):

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        
# leetcode submit region end(Prohibit modification and deletion)
