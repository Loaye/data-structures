"""Create a Max Heap."""


class Node(object):
    """Create a node object."""

    def __init__(self, data, node_left, node_right, parent):
        """Initialize a new node."""
        self.data = data
        self.node_left = node_left
        self.node_right = node_right
        self.parent = parent


class BinaryHeap(object):
    """Instantiates a heap organized by max data values."""

    def __init__(self, items=[]):
        """."""
        for i in items:
            self.heap.append(i)
            self.__floatUp(len(self.heap) - 1)

    def push(self, data):
        """Push a node into a heap using breadth first."""
        self.heap.data(data)
        self.__floatup(len(self.heap) - 1)

    def pop(self):
        """Pop the head, or the largest value, off the heap."""
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    def peek(self):
        """See the value in the top node, if there is one."""
        if self.heap[1]:
            return self.heap[1]
        else:
            return "the list is empty, nothing the see here, move along."

    def __swap(self, i, j):
        """Swap 2 nodes in the heap for sorting purposes."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __float_up(self, index):
        """Float the child above the parent if the value is greater."""
        parent = index // 2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbledown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbledown(largest)
