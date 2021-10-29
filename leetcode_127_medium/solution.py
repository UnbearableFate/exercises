from typing import List

class state:
    def __init__(self, v= ''):
        self.value = v
        self.distance = 0 #define as amount of different letters
        self.next = None
        self.step = 0
    def setDistance(self, target):
        dis = 0
        if len(self.value) != len(target.value) :
            return None
        for i in range(len(self.value)):
            if self.value[i] != target.value[i] :
                dis += 1
        self.distance = dis
        return self.distance

    def calDistance(self, otherString):
        dis = 0
        if len(self.value) != len(otherString) :
            return None
        for i in range(len(self.value)):
            if self.value[i] != otherString[i] :
                dis += 1
        return dis


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        startState = state(endWord)
        endState = state(beginWord)
        startState.setDistance(endState)
        startState.step = 1
        dis2BegRank = [[] for _ in range(len(beginWord)+1)]
        for word in wordList :
            if word == startState.value :
                continue
            dis = endState.calDistance(word)
            if dis :
                dis2BegRank[dis].append(word)
        dis2BegRank[0] = [beginWord]

        current = startState
        while current.distance != 0:
            findOk = False
            for index in range(current.distance-1, len(dis2BegRank)):
                for word in dis2BegRank[index] :
                    if current.calDistance(word) == 1 :
                        nextState = state(word)
                        nextState.distance = index
                        nextState.step = current.step +1
                        current.next = nextState
                        current = current.next
                        dis2BegRank[index].remove(word)
                        findOk = True
                        break
                if findOk:
                    break
            if not findOk:
                return 0
        return current.step

if __name__ == '__main__':
    ss = Solution()
    print(ss.ladderLength("hot","dog",["hot","dog"]))