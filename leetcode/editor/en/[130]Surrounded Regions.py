# # Given an m x n matrix board containing 'X' and 'O', capture all regions 
# that 
# # are 4-directionally surrounded by 'X'. 
# # 
# # A region is captured by flipping all 'O's into 'X's in that surrounded 
# # region. 
# # 
# # 
# # Example 1: 
# # 
# # 
# # Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X",
# # "O","X","X"]]
# # Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X",
# 
# # "X"]]
# # Explanation: Surrounded regions should not be on the border, which means 
# that 
# # any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is 
# not 
# # on the border and it is not connected to an 'O' on the border will be 
# flipped to 
# # 'X'. Two cells are connected if they are adjacent cells connected 
# horizontally 
# # or vertically.
# # 
# # 
# # Example 2: 
# # 
# # 
# # Input: board = [["X"]]
# # Output: [["X"]]
# # 
# # 
# # 
# # Constraints: 
# # 
# # 
# # m == board.length 
# # n == board[i].length 
# # 1 <= m, n <= 200 
# # board[i][j] is 'X' or 'O'. 
# # 
# # Related Topics Array Depth-First Search Breadth-First Search Union Find 
# # Matrix 👍 4793 👎 1199
# 

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if len(board) <= 2 or (len(board) > 0 and len(board[0]) <= 2):
            return
        m = len(board)
        n = len(board[0])
        groupOfPoint = dict()
        pointGroup = dict()
        pointGroup[0] = set()
        index = 1
        for i in range(0, m):
            if board[i][0] == 'O':
                pointGroup[0].add((i, 0))
                groupOfPoint[(i, 0)] = 0
            if board[i][n - 1] == '0':
                pointGroup[0].add((i, n - 1))
                groupOfPoint[(i, n - 1)] = 0
        for j in range(0, n):
            if board[0][j] == 'O':
                pointGroup[0].add((0, j))
                groupOfPoint[(0, j)] = 0
            if board[m - 1][j] == 'O':
                pointGroup[0].add((m - 1, j))
                groupOfPoint[(m - 1, j)] = 0

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if board[i][j] == 'O':
                    nears = [None, None]
                    if board[i - 1][j] == 'O':
                        nears[0] = groupOfPoint[(i - 1, j)]
                    if board[i][j - 1] == 'O':
                        nears[1] = groupOfPoint[(i, j - 1)]

                    if (i + 1 == m - 1 and board[i + 1][j] == 'O') or (j + 1 == n - 1 and board[i][j + 1] == 'O'):
                        groupOfPoint[(i, j)] = 0
                        pointGroup[0].add((i, j))
                        for k in [0, 1]:
                            if nears[k]:
                                for p in pointGroup[nears[k]]:
                                    groupOfPoint[p] = 0
                                pointGroup[0].update(pointGroup[nears[k]])
                                pointGroup.pop(nears[k])
                        continue

                    if nears[0] is not None and nears[1] is None:
                        groupOfPoint[(i, j)] = nears[0]
                        pointGroup[nears[0]].add((i, j))
                        continue
                    if nears[1] is not None and nears[0] is None:
                        groupOfPoint[(i, j)] = nears[1]
                        pointGroup[nears[1]].add((i, j))
                        continue
                    if nears[0] is None and nears[1] is None:
                        g = groupOfPoint[(i, j)] = index
                        index += 1
                        pointGroup[g] = set()
                        pointGroup[g].add((i, j))
                        continue

                    if nears[0] == nears[1]:
                        groupOfPoint[(i, j)] = nears[0]
                        pointGroup[nears[0]].add((i,j))
                    else:
                        nears.sort()
                        groupOfPoint[(i, j)] = nears[0]
                        pointGroup[nears[0]].add((i,j))
                        for p in pointGroup[nears[1]]:
                            groupOfPoint[p] = nears[0]
                        pointGroup[nears[0]].update(pointGroup[nears[1]])
                        pointGroup.pop(nears[1])
        for key, group in pointGroup.items():
            if key == 0:
                continue
            for p in group:
                board[p[0]][p[1]] = 'X'

        """
        Do not return anything, modify board in-place instead.
        """


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    ss = Solution()
    hh = [["X","O","O","X","X","X","O","X","O","O"],["X","O","X","X","X","X","X","X","X","X"],["X","X","X","X","O","X","X","X","X","X"],["X","O","X","X","X","O","X","X","X","O"],["O","X","X","X","O","X","O","X","O","X"],["X","X","O","X","X","O","O","X","X","X"],["O","X","X","O","O","X","O","X","X","O"],["O","X","X","X","X","X","O","X","X","X"],["X","O","O","X","X","O","X","X","O","O"],["X","X","X","O","O","X","O","X","X","O"]]
    ss.solve(hh)
    print(hh)
