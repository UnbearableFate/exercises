# Given an integer array nums, move all 0's to the end of it while maintaining 
# the relative order of the non-zero elements. 
# 
#  Note that you must do this in-place without making a copy of the array. 
# 
#  
#  Example 1: 
#  Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
#  Example 2: 
#  Input: nums = [0]
# Output: [0]
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -2³¹ <= nums[i] <= 2³¹ - 1 
#  
# 
#  
# Follow up: Could you minimize the total number of operations done? Related 
# Topics Array Two Pointers 👍 8899 👎 240


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        tail = len(nums) -1
        while tail >=0 and nums[tail] == 0:
            tail = tail-1
        head = 0
        while head < tail:
            if nums[head] == 0:
                for i in range(head+1, tail+1):
                    nums[i-1] = nums[i]
                nums[tail] = 0
                tail -= 1
                while nums[tail] == 0:
                    tail = tail - 1
            if nums[head] != 0:
                head += 1

        """
        Do not return anything, modify nums in-place instead.
        """
        
# leetcode submit region end(Prohibit modification and deletion)
