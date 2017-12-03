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

    def balance(self, root):
        """Return Int ."""
        if root is None:
            return 0
        else:
            return max(self.depth(root.left) - self.depth(root.right))

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

    def breath_first(self):
        """Traverse the BST by breath first method."""
        if self.root is None:
            raise ValueError('The tree is empty, no nodes to return.')
        bft = [self.root]
        while bft:
            current = bft.pop(0)
            if current.left:
                bft.append(current.left)
            if current.right:
                bft.append(current.right)
            yield current.data

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
        # empty tree
        if self.root is None:
            return False

        # data is in root node.
        elif self.root.val == data:
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

        # find node to remove
        while node and node.val != data:
            parent = node
            if data < node.val:
                node = node.leftChild
            elif data > node.val:
                node = node.rightChild

        # data not found.
        if node is None or node.val != data:
            return False

        # Remove node has no children
        elif node.leftChild is None and node.rightChild is None:
            if data < parent.val:
                parent.leftChild = None
            else:
                parent.rightChild = None
            return True

        # Section for having left child only.
        elif node.leftChild and node.rightChild is None:
            if data < parent.val:
                parent.leftChild = node.leftChild
            else:
                parent.rightChild = node.leftChild
            return True

        # Section for having Right child only.
        elif node.leftChild is None and node.rightChild:
            if data < parent.val:
                parent.leftChild = node.rightChild
            else:
                parent.rightChild = node.rightChild
            return True

        # node has left AND right children
        else:
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
                if delNode.val < delNodeParent.val:
                    delNodeParent.leftchild = None
                else:
                    delNodeParent.rightChild = None


if __name__ == '__main__':
    import timeit

    insert_time_ub = BinarySearchTree()
    num = (x for x in range(1000))
    insert_unbalanced = timeit.timeit(
        'insert_time_ub.insert(next(num))',
        setup='from __main__ import insert_time_ub, num',
        number=1000)

    search_time_ub = BinarySearchTree()
    for i in range(100):
        search_time_ub.insert(i)
    search_unbalanced = timeit.timeit(
        'search_time_ub.search(99)',
        setup='from __main__ import search_time_ub',
        number=1000)

    search_unbalanced_head = timeit.timeit(
        'search_time_ub.search(0)',
        setup='from __main__ import search_time_ub',
        number=1000)

    insert_time_b = BinarySearchTree()

    def insert_time(val):
        """."""
        if (500 + val) % 2 == 0:
            insert_time_b.insert(500 + val)
        else:
            insert_time_b.insert(500 - val)

    num_b = (x for x in range(1000))
    insert_balanced = timeit.timeit(
        'insert_time(next(num_b))',
        setup='from __main__ import insert_time, num_b',
        number=1000)

    search_time_b = BinarySearchTree()
    for i in range(1000):
        if (500 + i) % 2 == 0:
            search_time_b.insert(500 + i)
        else:
            search_time_b.insert(500 - i)

    search_balanced_leaf = timeit.timeit(
        'search_time_b.search(999)',
        setup='from __main__ import search_time_b',
        number=1000)

    search_balanced_head = timeit.timeit(
        'search_time_b.search(500)',
        setup='from __main__ import search_time_b',
        number=1000)

    print('The following time relates to worst case insert.')
    print('Insert unbalanced: {}'.format(insert_unbalanced))
    print('Insert balanced: {}'.format(insert_balanced))
    print('\nThe following time relates to worst case search.')
    print('Search unbalanced leaf: {}'.format(search_unbalanced))
    print('Search balanced leaf: {}'.format(search_balanced_leaf))
    print('\nThe following time relates to best base search.')
    print('Search unbalanced head: {}'.format(search_unbalanced_head))
    print('Search balanced head: {}'.format(search_balanced_head))
