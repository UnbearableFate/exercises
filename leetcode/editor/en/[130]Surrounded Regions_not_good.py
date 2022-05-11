# Given an m x n matrix board containing 'X' and 'O', capture all regions that 
# are 4-directionally surrounded by 'X'. 
# 
#  A region is captured by flipping all 'O's into 'X's in that surrounded 
# region. 
# 
#  
#  Example 1: 
# 
#  
# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X",
# "O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X",
# "X"]]
# Explanation: Surrounded regions should not be on the border, which means that 
# any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not 
# on the border and it is not connected to an 'O' on the border will be flipped to 
# 'X'. Two cells are connected if they are adjacent cells connected horizontally 
# or vertically.
#  
# 
#  Example 2: 
# 
#  
# Input: board = [["X"]]
# Output: [["X"]]
#  
# 
#  
#  Constraints: 
# 
#  
#  m == board.length 
#  n == board[i].length 
#  1 <= m, n <= 200 
#  board[i][j] is 'X' or 'O'. 
#  
#  Related Topics Array Depth-First Search Breadth-First Search Union Find 
# Matrix 👍 4793 👎 1199
from collections import deque
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if len(board) <= 2 or (len(board) > 0 and len(board[0]) <= 2):
            return
        m = len(board)
        n = len(board[0])
        notChangeSet = set()
        for i in range(0, m - 1):
            for j in range(0, n - 1):
                if board[i][j] == 'O' and (i, j) not in notChangeSet:
                    OSet = set()
                    queue = deque()
                    queue.append((i, j))
                    isChangeNeed = True
                    while len(queue) > 0:
                        top = queue.popleft()
                        x = top[0]
                        y = top[1]
                        OSet.add(top)
                        if x == m - 1 or x == 0 or y == n - 1 or y == 0:
                            isChangeNeed = False
                        if x - 1 >= 0 and board[x - 1][y] == 'O' and (x - 1, y) not in OSet:
                            queue.append((x - 1, y))
                        if y - 1 >= 0 and board[x][y - 1] == 'O' and (x, y - 1) not in OSet:
                            queue.append((x, y - 1))
                        if x + 1 < m and board[x + 1][y] == 'O' and (x + 1, y) not in OSet:
                            queue.append((x + 1, y))
                        if y + 1 < n and board[x][y + 1] == 'O' and (x, y + 1) not in OSet:
                            queue.append((x, y + 1))
                    if not isChangeNeed:
                        notChangeSet.update(OSet)
                        OSet.clear()
                    for o in OSet:
                        board[o[0]][o[1]] = 'X'

        """
        Do not return anything, modify board in-place instead.
        """


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    ss = Solution()
    hh = [["O", "X", "O", "O", "X", "X"],
          ["O", "X", "X", "X", "O", "X"],
          ["X", "O", "O", "X", "O", "O"],
          ["X", "O", "X", "X", "X", "X"],
          ["O", "O", "X", "O", "X", "X"],
          ["X", "X", "O", "O", "O", "O"]]
    ss.solve(hh)
    print(hh)
