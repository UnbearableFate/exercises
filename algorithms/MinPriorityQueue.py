import itertools
import sys
from heapq import heappush, heappop


class Vertex:
    def __init__(self, x=0, y=0, d=0):
        self.x = x
        self.y = y
        self.nextVertexPriorityMap = dict[Vertex, int]
        self.priority = d

    def __hash__(self):
        return hash(str(self.x) + '_' + str(self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.priority < other.priority

    @staticmethod
    def getHash(x,y=None):
        if y is None and (isinstance(x,list) or isinstance(x,tuple)):
            return hash(str(x[0])+'_'+str(x[1]))
        else:
            return hash(str(x)+'_'+str(y))


class MinPriorityQueue:
    def __init__(self):
        self.pq = []  # list of entries arranged in a heap
        self.vertex_finder = dict()  # mapping of tasks to entries
        self.REMOVED = '<removed-task>'  # placeholder for a removed task

    def add_node(self, v: Vertex):
        'Add a new task or update the priority of an existing task'
        if v.__hash__() in self.vertex_finder:
            self.remove_node((v.x, v.y))
        entry = [v.priority, v]
        self.vertex_finder[v.__hash__()] = v
        heappush(self.pq, entry)

    def remove_node(self, key):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        h = hash(str(key[0]) + '_' + str(key[1]))
        vertex = self.vertex_finder.pop(h)
        vertex = self.REMOVED  # 在这个只是把dict中的

    def pop_node(self)->Vertex:
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            priority, vertex = heappop(self.pq)
            if vertex is not self.REMOVED:
                del self.vertex_finder[vertex.__hash__()]
                return vertex
        raise KeyError('pop from an empty priority queue')

    def change_priority(self, position, pro):
        h = hash(str(position[0]) + '_' + str(position[1]))
        if h in self.vertex_finder:
            self.add_node(Vertex(position[0], position[1], pro))
            return 0
        else:
            return -1

    def get_priority(self, position):
        if Vertex.getHash(position) in self.vertex_finder:
            return self.vertex_finder[Vertex.getHash(position)].priority
        else:
            return sys.maxsize

    def __len__(self):
        return len(self.vertex_finder)

    def exists(self, position):
        return Vertex.getHash(position) in self.vertex_finder

def dijkstra(graph,target):
    n = len(graph)
    m = len(graph[0])
    queue = MinPriorityQueue()
    for i in range(0,n):
        for j in range(0,m):
            if graph[i][j] != 0:
                queue.add_node(Vertex(i,j,sys.maxsize))
    queue.change_priority((0,0),0)
    reached_nodes = set()
    while len(queue) > 0:
        top = queue.pop_node()
        if top.x == target[0] and top.y == target[1]:
            return top.priority
        possbityPos = [(top.x-1,top.y) , (top.x+1,top.y)
            , (top.x,top.y-1), (top.x,top.y+1) ]
        for pos in possbityPos:
            if queue.exists(pos):
                pri = queue.get_priority(pos)
                if pri > top.priority + 1:
                    queue.change_priority(pos,top.priority+1)
        reached_nodes.add(top)


if __name__ == '__main__':
    print(dijkstra([
        [1,0,0],
        [1,0,0],
        [1,9,1]
    ],(2,1)))
