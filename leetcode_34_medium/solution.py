from typing import List

def searchLeft(target, nums , begin, end) :
    if begin > end :
        return 0
    midleft = int((begin+end) /2)
    midright = int(midleft+1)
    if target > nums[midleft] and target < nums[midright] :
        return midright

    if target > nums[midright] :
        return searchLeft(target, nums, midright, end)

    if target < nums[midleft] :
        return searchLeft(target, nums,begin, midleft)

def searchRight(target, nums, begin, end):
    if begin >= end :
        return 0
    midleft = int((begin+end) /2)
    midright = int(midleft+1)
    if target > nums[midleft] and target < nums[midright] :
        return midleft

    if target > nums[midright] :
        return searchRight(target, nums, midright, end)

    if target < nums[midleft] :
        return searchRight(target, nums,begin, midleft)

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [0,0]
        if len(nums) <= 0 or target < nums[0] or target > nums[len(nums) - 1]:
            return [-1, -1]
        nums = [nums[0]-1] + nums + [nums[len(nums)-1]+1]
        result[0] = searchLeft(target-0.5, nums, 0, len(nums)-1)
        result[1] = searchRight(target+0.5, nums, 0, len(nums)-1)
        if nums[result[0]] != target or nums[result[1]] != target :
            return [-1, -1]
        result[0] -= 1
        result[1] -= 1
        return result

if __name__ == '__main__':
    ss = Solution()
    print(ss.searchRange([2, 2], 2))