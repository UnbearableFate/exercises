from typing import List


class state:
    def __init__(self, v= ''):
        self.value = v
        self.distance = 0 #define as amount of different letters
        self.children = []
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
        if endWord not in wordList :
            return 0
        wordList.remove(endWord)
        startState = state(endWord)
        startState.step = 1
        endState = state(beginWord)
        startState.setDistance(endState)
        stack = []
        stack.append(startState)
        while stack and wordList:
            top = stack[0]
            stack = stack[1:]
            index = 0
            while index < len(wordList) :
                if top.calDistance(wordList[index]) == 1 :
                    newState = state(wordList[index])
                    newState.step = top.step+1
                    newState.setDistance(endState)
                    if newState.distance == 1:
                        return newState.step
                    top.children.append(newState)
                    stack.append(newState)
                    del wordList[index]
                else:
                    index += 1
        return 0

if __name__ == '__main__':
    ss = Solution()
    print(ss.ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"]))