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
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        left = up = 0
        down = len(matrix) - 1
        right = len(matrix[0]) - 1
        result = []
        i = j = 0
        state = 'right'
        while True:
            result.append(matrix[i][j])
            nex = feasibilityCheck(i, j, state, left, right, up, down)
            print(nex)
            if len(nex) == 0:
                break
            i = nex[0]
            j = nex[1]
            state = nex[2]
            left = nex[3]
            right = nex[4]
            up = nex[5]
            down = nex[6]
        return result


if __name__ == '__main__':
    ss = Solution()
    ma = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    print(ss.spiralOrder(ma))
