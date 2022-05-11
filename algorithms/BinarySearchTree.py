from leetcode.editor.en.UsefulClass import TreeNode


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,z:TreeNode):
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.val < x.val :
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            self.root = z
        else:
            if z.val < y.val:
                y.left = z
            else:
                y.right = z

