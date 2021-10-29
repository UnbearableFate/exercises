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

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root :
            return False
        q = []
        q.append(root)
        while q :
            curr = q[0]
            if not curr.left and not curr.right :
                if curr.val == sum :
                    return True
            q = q[1:]
            if curr.left :
                curr.left.val += curr.val
                if curr.left.val <= sum :
                    q.append(curr.left)

            if curr.right :
                curr.right.val += curr.val
                if curr.right.val <= sum :
                    q.append(curr.right)
        return False
if __name__ == '__main__':
    ss = Solution()
    print(ss.hasPathSum())