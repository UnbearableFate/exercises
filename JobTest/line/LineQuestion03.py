class state:
    def __init__(self):
        self.content = ""
        self.v = 0
        self.l = 0

    def addLeft(self, ori):
        self.content = ori.content + "("
        self.v = ori.v + 1
        self.l = ori.l - 1

    def addRight(self, ori):
        self.content = ori.content + ")"
        self.v = ori.v - 1
        self.l = ori.l


class myqueue:
    def __init__(self):
        self.value = []

    def empty(self):
        return (len(self.value) == 0)

    def get(self):
        res = self.value[0]
        self.value = self.value[1:]
        return res

    def put(self, a):
        self.value.append(a)


class Solution(object):
    def generateParenthesis(self, n):
        q = myqueue()
        rootState = state()
        rootState.content = ""
        rootState.v = 0
        rootState.l = n
        q.put(rootState)
        result = set()
        while not q.empty():
            current = q.get()
            if current.l > 0:
                newStateAddLeft = state()
                newStateAddLeft.addLeft(current)
                q.put(newStateAddLeft)
            if current.v > 0:
                newStateAddRight = state()
                newStateAddRight.addRight(current)
                q.put(newStateAddRight)
            if current.l == 0 and current.v == 0:
                result.add(current.content)
        return list(result)