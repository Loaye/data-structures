"""Create a Max Heap."""


class Node(object):
    """Create a node object."""

    def __init__(self, data, node_left, node_right, parent):
        """Initialize a new node."""
        self.data = data
        self.node_left = node_left
        self.node_right = node_right
        self.parent = parent


class Binheap(object):
    """Instantiates a heap organized by max data values."""

    def __init__(self):
        """."""
        self.heap = []

    def push(self, data):
        """Push a node into a heap using breadth first."""
        pass
