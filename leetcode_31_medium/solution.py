from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]):
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return

        for i in range(len(nums)-2 , -1, -1) : #从尾部搜索，试图让 oldHead->x->...变大一点
            oldHeadNum = nums[i]
            ok = False
            for lb in range(oldHeadNum+1, 10) : # i位置之后有没有比nums[i]刚好大一点的呢
                try:
                    ii = nums.index(lb, i, len(nums))
                    temp = nums[ii]
                    nums[ii] = nums[i]
                    nums[i] = temp
                    #开始计数排序
                    ctDict = dict()
                    for j in range(10):
                        ctDict[j] = nums[i+1:].count(j)
                    index = i+1
                    for n, ct in ctDict.items():
                        for k in range(ct):
                            nums[index] = n
                            index = index+1
                    #基数排序完成
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
    print(ss.nextPermutation([1,3,2]))