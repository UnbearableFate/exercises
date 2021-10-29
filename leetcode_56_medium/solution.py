from typing import List



class tree:
    def __init__(self, root = None):
        self.root = root

    def search(self, node):

    def insert(self, node):



class treeNode:
    def __init__(self,b= 0, e=0):
        self.begin = b
        self.end = e
        self.left = None
        self.right = None
        self.parent = None

    def getNext(self):
        if not self.parent :
            p = self
            while p.left :
                p = p.left
            return p
        else:
            p = self.parent.right
            if not p :
                return self.parent
            else:
                while p.left :
                    p = p.left
                return p

def rightMerge(node: treeNode) :
    nex = node.getNext()
    while nex.begin <= node.end :
        if nex == node.parent :
            node.parent.begin = min(node.begin,node.parent.begin)
            node.parent.end = max(node.end, node.parent.end)
            nnext = node.parent.getNext()
            del node
            node = node.parent
            nex = nnext
        else:
            node.end = max(node.end, nex.end)
            nnext = nex.getNext()
            del nex
            nex = nnext

def leftMerge(node: treeNode):
    forword = node
    if node.left :
        forword = node.parent
        while forword.left


def searchAndInsert(parent:treeNode, node:treeNode) :
    if node.begin <= parent.begin :
        if parent.left :
            searchAndInsert(parent.left, node)
        else:
            parent.left = node
            rightMerge(node)

    if no

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
