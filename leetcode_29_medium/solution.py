from math import *
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        dividendPlus = True
        divisorPlus = True
        allPlus = True
        if dividend >= 0 :
            dividendPlus = True
        else:
            dividendPlus = False
            dividend = -dividend

        if divisor > 0 :
            divisorPlus = True
        else:
            divisorPlus = False
            divisor = -divisor
        if dividend == 0 :
            return  0
        ct = log(dividend) - log(divisor)
        ct = exp(ct)

        if (dividendPlus and divisorPlus) or (not divisorPlus and not dividendPlus) :
            ct = ct
        else:
            ct = -ct

        return ct

if __name__ == '__main__':
    ss = Solution()
    print(ss.divide(2147483648,1))
