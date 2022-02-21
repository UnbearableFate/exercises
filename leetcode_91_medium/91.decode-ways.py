#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 :
            return 0
        opt = [0 for i in range(0,len(s)+1)]
        opt[0] = 1
        if int(s[0]) > 0:
            opt[1] = 1
        for i in range(1, len(s)):
            v1 = 0
            v2 = 0
            if int(s[i]) > 0:
                v1 = opt[i]
            if i-1 >= 0 and (int(s[i-1:i+1]) >=10 and int(s[i-1:i+1]) <=26) :
                v2 = opt[i-1]
            opt[i+1] = v1+v2
        return opt[len(s)]
# @lc code=end

if __name__ == "__main__":
    ss = Solution()
    