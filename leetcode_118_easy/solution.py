from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0 :
            return []
        if numRows == 1 :
            return [[1]]
        res = [[1]]
        for i in range(1, numRows) :
            rowmax = int(i / 2)
            newLine = [1]
            for j in range(1,rowmax+1) :
                newLine.append(res[i-1][j-1]+res[i-1][j])
            if i % 2 == 0:
                newLine.extend(reversed(newLine[:rowmax]))
            else:
                newLine.extend(reversed(newLine))
            res.append(newLine)
        return res

if __name__ == '__main__':
    ss = Solution()
    print(ss.generate(9))