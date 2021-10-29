from typing import List

subStruct = dict()

class my_list(list):
    def __init__(self, ll):
        super().__init__(ll)
    def __hash__(self):
        res = ''
        for v in self :
            res += str(v)+','
        return hash(res)
    def __eq__(self, other):
        if len(self) != len(other) :
            return False
        for i in range(len(self)):
            if self[i] != other[i] :
                return  False
        return True

    def remov(self, i):
        return my_list(self[:i] + self[i+1:])

def _permute(nums):
    result = set()
    if len(nums) == 1 :
        result.add(nums)
        return result

    for i in range(len (nums)):
        for li in _permute(nums.remov(i)) :
            newone = my_list([nums[i]]+li)
            if newone not in result :
                result.add(newone)
    return result

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nn = my_list(nums)
        return _permute(nn)

if __name__ == '__main__':
    ss = Solution()
    print(ss.permute([1,1,2]))