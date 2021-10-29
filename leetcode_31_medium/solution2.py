from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]):
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        maxNum = max(nums)
        for i in range(len(nums)-2 , -1, -1) : #从尾部搜索，试图让 oldHead->x->...变大一点
            oldHeadNum = nums[i]
            ok = False
            for lb in range(oldHeadNum+1, maxNum+1) : # i位置之后有没有比nums[i]刚好大一点的呢
                try:
                    ii = nums.index(lb, i, len(nums))
                    temp = nums[ii]
                    nums[ii] = nums[i]
                    nums[i] = temp
                    nums[i+1:] = sorted(nums[i+1:])
                    ok = True
                    break
                except:
                    continue
            if ok:
                return nums
        nums.sort()
        return nums

if __name__ == '__main__':
    ss = Solution()
    print(ss.nextPermutation([16,27,25,23,25,16,12,9,1,2,7,20,19,23,16,0,6,22,16,11,8,27,9,2,20,2,13,7,25,29,12,12,18,29,27,13,16,1,22,9,3,21,29,14,7,8,14,5,0,23,16,1,20]))