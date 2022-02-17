
from pickletools import read_unicodestring4


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val == None:
            self.val = val
            return

        if self.val == val:
            return

        if self.val < val:
            if self.right:
                self.right.insert(val)
                return
            self.right = Node(val)
            return

        if self.left:
            self.left.insert(val)
            return
        self.left = Node(val)
        return

    def print(self):
        if self.val:
            if self.left:
                self.left.print()
            print(self.val)
            if self.right:
                self.right.print()

    def search(self, val):
        if self.val:
            if self.val == val:
                return True

            if val < self.val:
                if self.left == None:
                    return False
                return self.left.search(val)

            if val > self.val:
                if self.right == None:
                    return False
                return self.right.search(val)


r = Node(5)
r.insert(15)
r.insert(30)
r.insert(71)
r.insert(59)
r.insert(11)

r.print()
print(r.search(14))
