from typing import List

def find(target ,nums, begin, end) :
    if begin > end :
        return -1
    mid = int((begin + end) / 2)

    if target == nums[mid] :
        return mid
    if nums[begin] < nums[end]:
        if target < nums[mid] :
            return find(target, nums, begin, mid-1)
        else :
            return find(target, nums, mid+1 ,end)

    if nums[mid] < nums[begin] :
        if target < nums[mid] :
            return find(target, nums, begin, mid -1)
        else:
            if target > nums[end] :
                return find(target, nums, begin, mid -1)
            else:
                return find(target, nums, mid+1, end)
    else:
        if target < nums[mid] :
            if target < nums[begin] :
                return find(target, nums, mid+1, end)
            else:
                return find(target, nums, begin, mid-1)
        else:
            return find(target, nums, mid+1, end)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return find(target, nums, 0, len(nums)-1)

if __name__ == '__main__':
    sol = Solution()
    print(sol.search([4,5,6,7,8,1,2,3],8))
