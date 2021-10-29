#It is a worry notAGoodSolution.py, but I solve it by c++
class Solution:
    def removeDuplicates(self, nums) -> int:
        tag = nums[0]-1
        if len(nums) <= 1 :
            return len(nums)
        i = 1
        while i < len(nums) and nums[i] != tag :
            if nums[i] == nums[i-1]:
                j = i
                while j < len(nums) -1 and nums[j] != tag:
                    nums[j] = nums[j+1]
                    j = j +1
                nums[j] = tag
            else:
                i = i+1
        nums = nums[:i]
        return len(nums), nums

ss = Solution()
aaa = [1,2]
print(ss.removeDuplicates(aaa))