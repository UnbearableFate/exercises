#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
from copy import deepcopy
import string
from unittest import result


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        res.append([])
        p = 0
        while p < len(nums):
            res.append([nums[p]])
            p += nums.count(nums[p])
        basePos = 1
        while basePos < len(res) and len(res[basePos]) < len(nums):
            v = res[basePos]
            tail = v[len(v)-1]
            newItemPos = nums.index(tail) + v.count(tail)
            while newItemPos < len(nums):
                temp = deepcopy(v)
                temp.append(nums[newItemPos])
                res.append(temp)
                newItemPos += nums.count(nums[newItemPos])-v.count(nums[newItemPos])
            basePos += 1
        return res
# @lc code=end

if __name__ == "__main__" :
    Solution.subsetsWithDup([1,2,2])