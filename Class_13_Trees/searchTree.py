
from numpy import insert


class Node:

    def __init__(self, key):
        self.val = key
        self.right = None
        self.left = None

    def insert(root, key):
        if root is None:
            return Node(key)
        else:
            if root.val == key:
                return root
            elif root.val < key:
                root.right = insert(root.right, key)
            else:
                root.left = insert(root.left, key)
        return root

    def contains(self, key):
        if (key == self.val):
            return True
        elif (key < self.val):
            if (self.left == None):
                return False
            else:
                return self.left.contains(key)
        else:
            if (self.right == None):
                return False
            else:
                return self.right.contains(key)


r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

print(r.contains)
