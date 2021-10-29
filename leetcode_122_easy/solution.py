from typing import List

def noMinus(a,b) :
    if a - b < 0 :
        return 0
    else:
        return a - b
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0 :
            return 0
        buy = 0
        hold = False
        sell = 0
        sum = 0
        for date in range(0,len(prices)) :
            if hold :
                if date + 1 == len(prices) or prices[date+1] < prices[date] :
                    sum += noMinus(prices[date], prices[buy])
                    hold = False
            else:
                if date + 1 == len(prices) or prices[date+1] < prices[date] :
                    continue
                else:
                    buy = date
                    hold = True
        return sum

if __name__ == '__main__':
    ss = Solution()
    print( ss.maxProfit([1,2,3,4,5]))