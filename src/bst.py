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
        if root is None:
            return 0
        else:
            return max(self.depth(root.left) - self.depth(root.right))

    def in_order(self):
        """Traverse the bst nodes in order."""
        if self.root is None:
            raise ValueError("Tree is empty.")
        curr = self.root
        order = []
        while curr or order:
            if curr:
                order.append(curr)
                curr = curr.left
            else:
                curr = order.pop()
                yield curr.val
                curr = curr.right

    def pre_order(self):
        """Traverse the bst nodes by pre order."""
        if self.root is None:
            raise ValueError("Tree is empty.")
        curr = self.root
        order = []
        while curr or order:
            if curr:
                yield curr.value
                if curr.right:
                    order.append(curr.right)
                curr = curr.left
            else:
                curr = order.pop()

    def post_order(self):
        """Traverse the bst nodes in post order."""
        if self.root is None:
            raise ValueError("Tree is empty.")
        curr = self.root
        child = None
        order = []
        while curr or order:
            if curr:
                order.append(curr)
                curr = curr.left
            else:
                if order[-1].right and order[-1].right is not child:
                    curr = order[-1].right
                else:
                    child = order.pop()
                    yield child.value

    def delete(self, data):
        """Remove a node from the BST."""
        if self.root is None:  # empty tree
            return False
        elif self.root.val == data:  # data is in root node.
            if self.root.leftChild is None and self.root.rightChild is None:
                self.root = None
            elif self.root.leftChild and self.root.rightChild is None:
                self.root = self.root.leftChild
            elif self.root.leftChild is None and self.root.rightChild:
                self.root = self.root.rightChild
            elif self.root.leftChild and self.root.rightChild:
                delNodeParent = self.root
                delNode = self.root.rightChild
                while delNode.leftChild:
                    delNodeParent = delNode
                    delNode = delNode.leftChild

                self.root.val = delNode.val
                if delNode.rightChild:
                    if delNodeParent.val > delNode.val:
                        delNodeParent.leftChild = delNode.rightChild
                    elif delNodeParent.val < delNode.rightChild:
                        delNodeParent.rightChild = delNode.rightChild
                else:
                    if delNode.val < delNodeParent.val:
                        delNodeParent.leftChild = None
                    else:
                        delNodeParent.rightChild = None

            return True

        parent = None
        node = self.root

        while node and node.val != data:  # find node to remove
            parent = node
            if data < node.val:
                node = node.leftChild
            elif data > node.val:
                node = node.rightChild

        if node is None or node.val != data:  # data not found.
            return False

        elif node.leftChild is none and left child.rightChild is None:  # Remove node has no children
            if data < parent.val:
                parent.leftChild = None
            else:
                parent.rightChild = None
            return True

        elif node.leftChild and node.rightChild is None:  # Section for having left child only.
            if data < parent.val:
                parent.leftChild = node.leftChild
            else:
                parent.rightChild = node.leftChild
            return True

        elif node.leftChild is None and node.rightChild:  # Section for having Right child only.
            if data < parent.val:
                parent.leftChild = node.rightChild
            else:
                parent.rightChild = node.rightChild
            return True

        else:  # node has left AND right children
            delNodeParent = node
            delNode = node.rightChild
            while delNode.leftChild:
                delNodeParent = delNode
                delNode = delNode.leftChild

            node.val = delNode.val
            if delNode.rightChild:
                if delNodeParent.val > delNode.val:
                    delNodeParent.leftChild = delNode.rightChild
                elif delNodeParent.val < delNode.val:
                    delNodeParent.rightChild = delNode.rightChild
            else:
                if delNode.val < dalNodeParent.val:
                    delNodeParent.leftchild = None
                else:
                    delNodeParent.rightChild = None

                    
if __name__ == '__main__':
