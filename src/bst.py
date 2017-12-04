"""Binary Search Tree."""


class Node(object):
    """Create Node class for BST."""

    def __init__(self, data):
        """Initialization of node class object."""
        self.data = data
        self.left = None
        self.right = None
        self.depth = 0
        self.parent = None


class BST(object):
    """Create Binary Search Tree."""

    def __init__(self, iterable=()):
        """Initialization of BST class object."""
        self.root = None
        self._size = 0
        self.layers = 0
        self.right_layers = 0
        self.left_layers = 0

        if isinstance(iterable, (tuple, list)):
            for i in iterable:
                self.insert(i)
        else:
            self.insert(iterable)

    def insert(self, data):
        """Add node to tree."""
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            self._size += 1
            return

        curr = self.root
        while curr:
            if new_node.data == curr.data:
                return "Duplicate data"

            if new_node.data < curr.data:
                if not curr.left:
                    new_node.depth = curr.depth + 1
                    curr.left = new_node
                    new_node.parent = curr
                    self._size += 1
                    break
                curr = curr.left
            elif new_node.data > curr.data:
                if not curr.right:
                    new_node.depth = curr.depth + 1
                    curr.right = new_node
                    new_node.parent = curr
                    self._size += 1
                    break
                curr = curr.right

        if new_node.depth > self.layers:
            self.layers = new_node.depth

        if (
                new_node.data > self.root.data and
                new_node.depth > self.right_layers
        ):
            self.right_layers += 1
        elif (
                new_node.data < self.root.data and
                new_node.depth > self.left_layers
        ):
            self.left_layers += 1

    def search(self, data):
        """Return node with specified data, or None."""
        curr = self.root
        while curr:
            if curr.data == data:
                return curr
            elif data < curr.data:
                curr = curr.left
            elif data > curr.data:
                curr = curr.right
        return

    def delete(self, data):
        """Delete node with specified data."""
        target = self.search(data)
        if not target:
            return

        if not target.left and not target.right:
            if not target.parent:
                self.root = None
            elif target.data > target.parent.data:
                target.parent.right = None
            else:
                target.parent.left = None

        elif target.left and target.right:
            curr = target.right
            while curr and curr.left:
                curr = curr.left
            print(curr.data)

            if curr.right:
                curr.parent.left = curr.right
            if target.right != curr:
                curr.right = target.right
            curr.left = target.left

            if not target.parent:
                self.root = curr
                curr.parent = None
            else:
                if target.data > target.parent.data:
                    target.parent.right = curr
                else:
                    target.parent.left = curr
                curr.parent = target.parent

        else:
            if target.left:
                child = target.left
            else:
                child = target.right

            if not target.parent:
                self.root = child
                child.parent = None
            else:
                child.parent = target.parent
                if target.data > target.parent.data:
                    target.parent.right = child
                else:
                    target.parent.left = child

        self._size -= 1
        return target.data

    def size(self):
        """Return number of nodes in tree."""
        return self._size

    def contains(self, data):
        """Return True if value in tree, else False."""
        return bool(self.search(data))

    def depth(self):
        """Return the number of layers deep in the tree."""
        return self.layers

    def balance(self):
        """Return 0 if balanced, 1 or -1 if unbalanced."""
        return self.left_layers - self.right_layers

    def in_order(self):
        """Put tree values into a list in order."""
        if not self.root:
            return 'Tree empty'

        curr = self.root
        order = []

        def gen_in_order(curr):
            """In order generator helper function."""
            if curr:
                gen_in_order(curr.left)
                if curr.data not in order:
                    order.append(curr.data)
                gen_in_order(curr.right)

        gen_in_order(curr)

        return self.traversal_generator(order)

    def pre_order(self):
        """Put tree values into a list using pre-order traversal."""
        if not self.root:
            return 'Tree empty'

        curr = self.root
        order = []

        def gen_pre_order(curr):
            """Pre order generator helper function."""
            if curr:
                if curr.data not in order:
                    order.append(curr.data)
                gen_pre_order(curr.left)
                gen_pre_order(curr.right)

        gen_pre_order(curr)
        return self.traversal_generator(order)

    def post_order(self):
        """Put tree values into a list using post-order traversal."""
        if not self.root:
            return 'Tree empty'

        curr = self.root
        order = []

        def gen_post_order(curr):
            if curr:
                gen_post_order(curr.left)
                gen_post_order(curr.right)
                order.append(curr.data)

        gen_post_order(curr)
        return self.traversal_generator(order)

    def breadth_first(self):
        """Put tree values into a list breadth-first."""
        if not self.root:
            return 'Tree empty'

        order = []
        route = [self.root]
        while route:
            curr = route.pop(0)
            order.append(curr.data)
            if curr.left:
                route.append(curr.left)
            if curr.right:
                route.append(curr.right)

        return self.traversal_generator(order)

    def traversal_generator(self, order):
        """Generator for tree traversals."""
        for i in order:
            yield i
