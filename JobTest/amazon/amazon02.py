import heapq
import itertools
import sys


def minimumDistance(area):
    pq = []  # list of entries arranged in a heap
    entry_finder = {}  # mapping of tasks to entries
    REMOVED = '<removed-task>'  # placeholder for a removed task
    counter = itertools.count()  # unique sequence count

    def add_task(task, priority=0):
        'Add a new task or update the priority of an existing task'
        if task in entry_finder:
            remove_task(task)
        count = next(counter)
        entry = [priority, count, task]
        entry_finder[task] = entry
        heapq.heappush(pq, entry)

    def remove_task(task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = entry_finder.pop(task)
        entry[-1] = REMOVED

    def pop_task():
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while pq:
            priority, count, task = heapq.heappop(pq)
            if task is not REMOVED:
                del entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')










    target = [0, 0]
    n = len(area)
    m = len(area[0])
    opt = dict()
    for i in range(0, len(area)):
        for j in range(0, len(area[0])):
            if area[i][j] == 9:
                target = [i, j]

    for i in range(0, len(area)):
        for j in range(0, len(area[0])):
            opt[i*n+j] = sys.maxsize

    opt[0] = 0
    while len(opt.items()) > 0:
        top = sorted(opt.items(),key= lambda x:x[1])[0]
        del opt[top[0]]
        w = top[1]
        key = top[0]
        point = [int(top[0]/n),top[0]%n]
        if point[0] == target[0] and point[1] == target[1]:
            return w
        if point[0] - 1 >= 0 and opt[key - n] > w + 1 and area[point[0] - 1][point[1]] != 0:
            opt[key - n] = w + 1
        if point[0] + 1 < n and opt[key + n] > w + 1 and area[point[0] + 1][point[1]] !=0:
            opt[key + n] = w + 1
        if point[1] - 1 >= 0 and opt[key + 1] > w + 1 and area[point[0]][point[1]-1] !=0:
            opt[key + 1] = w + 1
        if point[1] + 1 < m and opt[key - 1] > w + 1 and area[point[0]][point[1]+1] !=0:
            opt[key - 1] = w + 1
    return 0

if __name__ == '__main__':
    minimumDistance([
        [1,0,0],
        [1,0,0],
        [1,9,1]
    ])