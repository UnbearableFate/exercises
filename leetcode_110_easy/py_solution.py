# Definition for a binary tree node.

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Tree:
    def __init__(self):
        self.root = None

    def createTree(self, nums):
        self.root = TreeNode(val=nums[0])
        q = []
        q.append([self.root ,0])
        while q :
            pa , i = q[0]
            q = q[1:]
            if 2*i +1 < len(nums) and nums[2*i+1]:
                pa.left = TreeNode(nums[2*i+1])
                q.append([pa.left, 2*i+1])
            if 2*i +2 <len(nums) and nums[2*i+2]:
                pa.right = TreeNode(nums[2*i+2])
                q.append([pa.right, 2*i+2])
        return self.root

def treeWalker(node: TreeNode) :
    heightList = None
    balanced = True

    if not node :
        return [[0],True]

    if node.left :
        heightList,balanced = treeWalker(node.left)
    else:
        heightList = [0]
        balanced = True

    if node.right :
        temp , balanced = treeWalker(node.right)
        heightList.extend(temp)
    else:
        if len(heightList) == 0:
            heightList = [0,0]
        balanced = balanced and True

    for i in range(len(heightList)) :
        heightList[i] = heightList[i] +1

    if len(heightList) > 0 and max(heightList) - min(heightList) > 1 :
        balanced = False

    return heightList, balanced

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        _ , bla = treeWalker(root)
        return bla

if __name__ == '__main__':
    tt = Tree()
    #tt.createTree([1,None,2,None,3])
    root = TreeNode(val=1, right=TreeNode(val=3, left=TreeNode(val=2)))
    ss = Solution()
    print(ss.isBalanced(root))