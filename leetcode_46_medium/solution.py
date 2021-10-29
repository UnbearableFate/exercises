from typing import List

subStruct = dict()

def _permute(nums):
    result = []
    if len(nums) == 1 :
        return [nums]

    for i in range( len(nums)) :
        for li in _permute(nums[:i]+nums[i+1:]) :
            result.append([nums[i]]+li)
    return result

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return _permute(nums)

if __name__ == '__main__':
    ss = Solution()
    print(ss.permute([1,1,2]))