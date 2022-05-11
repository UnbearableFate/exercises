# Given an unsorted array of integers nums, return the length of the longest 
# consecutive elements sequence. 
# 
#  You must write an algorithm that runs in O(n) time. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. 
# Therefore its length is 4.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  
#  Related Topics Array Hash Table Union Find 👍 9147 👎 402
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ss = set()
        for n in nums:
            ss.add(n)

        for n in nums:

# leetcode submit region end(Prohibit modification and deletion)
