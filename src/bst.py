"""Creatae a Binary Search Tree."""


class Node:
    """Tree node: left and right child & data which can be any object."""

    def __init__(self, val=None):
        """Initialize the BST data Structure."""
        self.left = None
        self.right = None
        self.val = val
        self.parent = None
        self._counter = 0


class BinarySearchTree:
    """Instantiates a BST."""

    def __init__(self):
            """Set the root."""
            self.root = None

    def insert(self, val):
        """Insert new node with data."""
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
                    self._counter += 1
            elif val > self.val:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
                    self._counter += 1
        else:
            self.val = val

    def search(self, val, parent=None):
        """Look up node containing data."""
        if val < self.val:
            if self.left is None:
                return None, None
            return self.left.search(val, self)
        elif val > self.val:
            if self.right is None:
                return None, None
            return self.right.lookup(val, self)
        else:
            return self, parent

    def size(self):
        """Return Int for the size of BST."""
        return self._counter

    def depth(self, root):
        """Return Int of # of levels below the root."""
        if root is None:
            return 0
        else:
            return max(self.depth(root.left), self.depth(root.right)) + 1

    def contains(self, val):
        """Return a boolean if val is in BST."""
        if self.root is not None:
            return self._search(val, self.root)
        elif self.val == val:
            return True
        elif val < self.val and self.left is not None:
            return self.left.val
        elif val < self.val and self.right is not None:
            return self.right.val
        return False

    def balance(self):
        """Return Int ."""
        pass

if __name__ == '__main__':

    root = Node(8)
    root.insert(5)
    root.insert(11)
    root.insert(1)
    root.insert(6)
    root.insert(3)
    root.insert(7)
    root.insert(15)
    root.insert(12)



