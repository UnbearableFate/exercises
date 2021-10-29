from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastEnd = 0;
        thisEnd = nums[0]
        while thisEnd < len(nums) -1 :
            nextEnd = thisEnd
            for n in range(lastEnd+1, thisEnd+1) :
                ssum = n+ nums[n]
                if ssum > nextEnd :
                    nextEnd = ssum
            lastEnd = thisEnd
            thisEnd = nextEnd
            if thisEnd == lastEnd :
                return False
        return True

if __name__ == '__main__':
    ss = Solution()
    print(ss.canJump([3,2,1,0,4]))