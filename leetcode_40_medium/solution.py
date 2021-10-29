from typing import List
import copy

class state :
    sortedKeys = []
    def __init__(self):
        self.combo = []
        self.children = []
        self.color = 0
        self.possbileNextStep = dict()
        self.diff = 0
        self.childPoint = 0

    def setDiff(self, target = 0):
        ss = sum(self.combo)
        self.diff = target - ss

    def createChildren(self):
        if sum(self.possbileNextStep.values()) == 0 :
            return False
        begin = 0
        if len(self.combo) > 0 :
            begin = state.sortedKeys.index(self.combo[len(self.combo)-1])
        for i in range(begin, len(state.sortedKeys)) :
            key = state.sortedKeys[i]
            if self.diff >= key and self.possbileNextStep[key] > 0:
                newChild = state()
                newChild.combo = copy.deepcopy(self.combo)
                newChild.combo.append(key)
                newChild.diff = self.diff - key
                newChild.possbileNextStep = copy.deepcopy(self.possbileNextStep)
                newChild.possbileNextStep[key] -= 1
                for kk in state.sortedKeys :
                    if kk > newChild.diff :
                        newChild.possbileNextStep[kk] = 0
                self.children.append(newChild)
        if len(self.children) == 0 :
            return False
        return True

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        initBase = dict()
        for c in candidates :
            if c not in initBase :
                initBase[c] = 1
            else:
                initBase[c] += 1
        sortedkeys = sorted(initBase.keys())
        state.sortedKeys = sortedkeys
        stack = []

        root = state()
        root.diff = target
        root.possbileNextStep = initBase

        result = []
        stack.append(root)
        while len(stack) > 0 :
            top = stack[len(stack)-1]
            if top.color == 2 :
                if top.diff == 0 :
                    result.append(top.combo)
                stack = stack[:len(stack)-1]
                continue

            if top.color == 1 :
                if top.childPoint < len(top.children) :
                    stack.append(top.children[top.childPoint])
                    top.childPoint += 1
                else:
                    top.color = 2
                continue

            if top.color == 0 :
                if top.createChildren():
                    top.color = 1
                else:
                    top.color = 2
                continue
        return result

if __name__ == '__main__':
    ss = Solution()
    print(ss.combinationSum2([10,1,2,7,6,1,5],8))



