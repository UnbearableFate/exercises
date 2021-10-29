import queue
from typing import List

STACK = []

class posision :
    def __init__(self, col = 0, row = 0, value = 0):
        self.col = col
        self.row = row
        self.value = value

class state:
    def __init__(self):
        self.board = []
        self.route = []
        self.currentPos = posision()
        self.children = []

    def init(self, bor):
        for line in bor:
            self.board.append([])
            for block in line:
                if block == '.':
                    self.board[len(self.board) - 1].append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
                else:
                    self.board[len(self.board) - 1].append(int(block))
        for i in range(9):
            for j in range(9):
                if isinstance(self.board[i][j], int):
                    continue
                for k in range(9):
                    if isinstance(self.board[i][k], int):
                        self.board[i][j][self.board[i][k]] = 0
                for k in range(9):
                    if isinstance(self.board[k][j], int):
                        self.board[i][j][self.board[k][j]] = 0
                rowbase = int(i / 3)
                colbase = int(j / 3)
                for x in range(3 * rowbase, 3 * rowbase + 3):
                    for y in range(3 * colbase, 3 * colbase + 3):
                        if isinstance(self.board[x][y], int):
                            self.board[i][j][self.board[x][y]] = 0

    def setValue(self, row, col, value):
        if isinstance(self.board[row][col], int):
            return False
        for k in range(9):
            if isinstance(self.board[row][k], int) or self.board[row][k][0] == 0:
                continue
            if self.board[row][k][value] <= 0:
                return False
            self.board[row][k][value] = 0
        for k in range(9):
            if isinstance(self.board[k][col], int) or self.board[k][col][0] == 0:
                continue
            if self.board[k][col][value] <= 0:
                return False
            self.board[k][col][value] = 0
        rowbase = int(row / 3)
        colbase = int(col / 3)
        for x in range(3 * rowbase, 3 * rowbase + 3):
            for y in range(3 * colbase, 3 * colbase + 3):
                if isinstance(self.board[x][x], int) or self.board[x][y][0] == 0:
                    continue
                self.board[x][y][value] = 0
        self.board[row][col][value] = -1
        self.board[row][col][0] = 0
        return True

    def goNext(self):
        for i in range(self.currentPos.row , 9) :
            for j in range(self.currentPos.col, 9) :
                if isinstance(self.board[i][j], int) or self.board[i][j][0] == 0:
                    continue
                for v in range(1,10) :
                    if self.board[i][j][v] > 0 :
                        if self.setValue(i,j,v) :
                            STACK.append(self)
                            return




bb = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
ss = state(bb)
print("")


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rootState = state()
        rootState.init(board)
        qq = queue.Queue()

