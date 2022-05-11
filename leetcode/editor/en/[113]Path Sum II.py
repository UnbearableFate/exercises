# Given the root of a binary tree and an integer targetSum, return all root-to-
# leaf paths where the sum of the node values in the path equals targetSum. Each 
# path should be returned as a list of the node values, not node references. 
# 
#  A root-to-leaf path is a path starting from the root and ending at any leaf 
# node. A leaf is a node with no children. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# Explanation: There are two paths whose sum equals targetSum:
# 5 + 4 + 11 + 2 = 22
# 5 + 8 + 4 + 5 = 22
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1,2,3], targetSum = 5
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: root = [1,2], targetSum = 0
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 5000]. 
#  -1000 <= Node.val <= 1000 
#  -1000 <= targetSum <= 1000 
#  
#  Related Topics Backtracking Tree Depth-First Search Binary Tree 👍 4638 👎 10
# 9


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List

# leetcode submit region begin(Prohibit modification and deletion)

from queue import Queue, SimpleQueue


class BigTreeNode:
    def __init__(self, node: TreeNode, parent=None):
        self.node = node
        self.val = node.val
        if parent:
            self.parent = parent
            self.sum = node.val + parent.sum
        else:
            self.parent = None
            self.sum = self.node.val


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        bigRoot = BigTreeNode(root)
        que = SimpleQueue()
        que.put(bigRoot)
        result = []
        while not que.empty():
            currentNode = que.get()
            if not currentNode.node.left and (not currentNode.node.right):
                if currentNode.sum == targetSum:
                    resultLine = [currentNode.node.val]
                    while currentNode.parent:
                        resultLine.append(currentNode.parent.node.val)
                        currentNode = currentNode.parent
                    resultLine.reverse()
                    result.append(resultLine)
                    continue

            if currentNode.node.left:
                myLeft = BigTreeNode(currentNode.node.left,currentNode)
                que.put(myLeft)
            if currentNode.node.right:
                myRight = BigTreeNode(currentNode.node.right, currentNode)
                que.put(myRight)

        return result

# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s =Solution()
    print( s.pathSum(TreeNode(-2, None, -3),-5))
