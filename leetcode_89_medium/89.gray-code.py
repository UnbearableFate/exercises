#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#

# @lc code=start
import re
from unittest import result
from math import pow
class Solution:
    def grayCode(self, n: int) -> List[int]:
        return self.gc(n)

    def gc(self,n:int)-> list:
        if n == 0 :
            return []
        if n == 1 :
            return [0,1]
        num = int(pow(2,n-1))
        res = self.gc(n-1)
        size = len(res)
        for i in range(size-1,-1,-1):
            res.append(res[i]+num)
        return res  
# @lc code=end