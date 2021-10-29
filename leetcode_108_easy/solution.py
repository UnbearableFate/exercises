# Definition for a binary tree node.
from typing import List


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def treeCreate(nums,begin, end) -> TreeNode :
    newRoot = TreeNode()
    if begin == end :
        newRoot.val = nums[begin]
        return newRoot
    if begin > end :
        return None

    mid = int((begin + end) / 2)
    newRoot.val = nums[mid]
    newRoot.left = treeCreate(nums, begin, mid-1)
    newRoot.right = treeCreate(nums, mid+1, end)
    return newRoot

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return treeCreate(nums, 0, len(nums)-1)

if __name__ == '__main__':
    ss = Solution()
    kk = ss.sortedArrayToBST([-10,-3,0,5,9])
    print(kk.val)