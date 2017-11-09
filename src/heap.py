"""Create a Max Heap."""

class BinaryHeap(object):
    """Instantiates a heap organized by max data values."""

    def __init__(self, iterable=[]):
        """."""
        self.heap = [0]
        self._counter = 0
        for i in iterable:
            self.heap.append(i)
            self._floatup(len(self.heap) - 1)

    def __len__(self):
        return len(self.heap)

    def push(self, data):
        """Push a node into a heap using breadth first."""
        self.heap.append(data)
        self._floatup(len(self.heap) - 1)

    def peek(self):
        """See the value in the top node, if there is one."""
        if self.heap[1]:
            return self.heap[1]
        else:
            return "The list is empty, nothing the see here, move along."

    def pop(self):
        """Pop the head, or the largest value, off the heap."""
        try:  
            if len(self.heap) > 2:
                self._swap(1, len(self.heap) - 1)
                max = self.heap.pop()
                self._bubbledown(1)
            elif len(self.heap) == 2:
                max = self.heap.pop()
            else:
                max = False
            return max
        except IndexError:
            raise IndexError("Can't pop from an empty list")

    def _swap(self, i, j):
        """Swap 2 nodes in the heap for sorting purposes."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _floatup(self, index):
        """Float the child above the parent if the value is greater."""
        parent = index // 2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self._swap(index, parent)
            self._floatup(parent)

    def _bubbledown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self._swap(index, largest)
            self._bubbledown(largest)

