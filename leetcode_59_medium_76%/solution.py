from typing import List

def feasibilityCheck(i, j, direction, left, right, up, down):
    if left > right or up > down:
        return []
    if direction == 'right':
        if j == right:
            return feasibilityCheck(i, j, 'down', left, right, up + 1, down)
        else:
            return [i, j + 1, 'right', left, right, up, down]

    if direction == 'down':
        if i == down:
            return feasibilityCheck(i, j, 'left', left, right - 1, up, down)
        else:
            return [i + 1, j, 'down', left, right, up, down]

    if direction == 'left':
        if j == left:
            return feasibilityCheck(i, j, 'up', left, right, up, down - 1)
        else:
            return [i, j - 1, 'left', left, right, up, down]

    if direction == 'up':
        if i == up:
            return feasibilityCheck(i, j, 'right', left + 1, right, up, down)
        else:
            return [i - 1, j, 'up', left, right, up, down]

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]
        left = up = 0
        down = n - 1
        right = n - 1
        i = j = 0
        num = 1
        state = 'right'
        while num <= n**2 :
            res[i][j] = num
            nex = feasibilityCheck(i, j, state, left, right, up, down)
            if len(nex) == 0:
                break
            i = nex[0]
            j = nex[1]
            state = nex[2]
            left = nex[3]
            right = nex[4]
            up = nex[5]
            down = nex[6]
            num += 1
        return res

if __name__ == '__main__':
    ss = Solution()
    print(ss.generateMatrix(2))