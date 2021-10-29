from typing import List
import copy
def swap(a,b):
    temp = a
    a = b
    b = temp

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0 :
            return
        n = len(matrix)
        center = (n-1) / 2
        i =0
        while i < center:
            j = i
            while j <= n-i-2 :
                pos = []
                pos.append( [i-center, j-center] )
                for k in range(3):
                    pos.append([pos[k][1],-pos[k][0]])

                for k in range(len(pos)):
                    pos[k][0] += center
                    pos[k][0] = round(pos[k][0])
                    pos[k][1] += center
                    pos[k][1] = round(pos[k][1])

                temp = copy.deepcopy(matrix[pos[3][0]][pos[3][1]])
                for k in range(2, -1 ,-1) :
                    matrix[pos[k+1][0]][pos[k+1][1]] = copy.deepcopy(matrix[pos[k][0]][pos[k][1]])
                matrix[pos[0][0]][pos[0][1]] = copy.deepcopy(temp)
                j += 1
            i += 1


if __name__ == '__main__':
    ss = Solution()
    matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]


    ss.rotate(matrix)

    print(matrix)