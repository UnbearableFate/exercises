class MyQueue:
    def __init__(self):
        self.data = dict()
        self.accessLog = []

    def updateAccess(self,k):
        if self.accessLog.count(k) > 0:
            self.accessLog.remove(k)
        self.accessLog.append(k)

    def add(self,k,v):
        self.data[k] = v
        self.updateAccess(k)

    def get(self, k):
        if k not in self.data :
            return '-1'
        else:
            self.updateAccess(k)
            return self.data[k]

    def remove(self,k):
        if k not in self.data :
            return '-1'
        else:
            self.accessLog.remove(k)
            return self.data.pop(k)

    def evict(self):
        if len(self.data.keys()) > 0:
            k = self.accessLog.pop(0)
            self.data.pop(k)



def solution(n):
    # write your code in Python
    result = []
    myQ = MyQueue()
    for cmd in n :
        cmd = cmd.split()
        if cmd[0] == "add" and len(cmd) == 3 :
            myQ.add(cmd[1],cmd[2])
            continue
        if cmd[0] == "get" and len(cmd) == 2 :
            result.append(myQ.get(cmd[1]))
            continue
        if cmd[0] == "remove" and len(cmd) == 2 :
            result.append(myQ.remove(cmd[1]))
            continue
        if cmd[0] == "evict" and len(cmd) == 1:
            myQ.evict()
            continue
        if cmd[0] == "exit":
            break

    return result
    pass

if __name__ == '__main__':
    print(solution(['add 5 3', 'add 1 2', 'get 5', 'evict', 'get 1', 'remove 5', 'exit']))