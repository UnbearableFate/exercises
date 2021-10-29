from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0 :
            return [1]
        last = [1]
        for i in range(1, rowIndex+1) :
            rowmax = int(i / 2)
            newLine = [1]
            for j in range(1,rowmax+1) :
                newLine.append(last[j-1]+last[j])
            if i % 2 == 0:
                newLine.extend(reversed(newLine[:rowmax]))
            else:
                newLine.extend(reversed(newLine))
            last = newLine
        return last

if __name__ == '__main__':
    ss = Solution()
    print(ss.getRow(5))