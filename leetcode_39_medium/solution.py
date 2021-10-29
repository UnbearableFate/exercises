import copy
STACK = []
RESULT = []

class state:
    def __init__(self):
        self.combo = []
        self.diff = 0
        self.color = 0
        self.possibleSteps = set()
        self.chilrenPoint = 0
        self.chilren = []

    def setDiff(self, target):
        self.diff = 0
        sum = 0
        for v in self.combo :
            sum = sum + v
        self.diff = target - sum

    def createChildren(self, candidate, target):
        limit = 0
        if len(self.combo) > 0:
            limit = self.combo[len(self.combo) - 1]
        for a in candidates :
            if a >= limit and a <= self.diff:
                waw = state()
                waw.combo = copy.deepcopy(self.combo)
                waw.combo.append(a)
                waw.setDiff(target)
                self.chilren.append(waw)

if __name__ == '__main__':
    target = 8
    candidates = [2, 3, 5]
    candidates.sort()
    root = state()
    root.setDiff(target)

    STACK.append(root)

    while len(STACK) != 0 :
        top = STACK[len(STACK)-1]
        if top.color == 2 :
            if top.diff == 0:
                RESULT.append(top.combo)
            STACK = STACK[:len(STACK)-1]
            continue
        if top.color == 0:
            top.color += 1
            top.createChildren(candidates, target)
            if len(top.chilren) > 0:
                STACK.append(top.chilren[top.chilrenPoint])
                continue
            else:
                top.color = 2
                continue
        if top.color == 1:
            top.chilrenPoint += 1
            if top.chilrenPoint >= len(top.chilren):
                top.color = 2
                continue
            else:
                STACK.append(top.chilren[top.chilrenPoint])

    print(RESULT)