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

"""
having items in a list, to detirmine its postition, use '//' to detirmine its
parent. Example: Put all nodes in a list, burn [0], so every node is in its
node position, [56, 45, 46, 34, 39, 40, 31, 21, 25, 29, 22, 23, 24, 28, 26],
where 56 is obviously in [1], 45 is [2] and so on. Then take [6] & [7], and //
2, which would be 3 for each (because of the //) so both are the child of [3].
Then compare [6] to [3] higher value is reassigned (or remains) [3]. If [6] was
NOT higher, then compare [7] to [3], and so on.

"""
