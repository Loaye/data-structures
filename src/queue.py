"""Implentation of a Queue."""


from dll import DoublyLinkedList


class Queue(object):
    """Creates a Queue class."""

    def __init__(self):
        """Initialization of the queue."""
        self._dll = DoublyLinkedList()
        self._counter = self._dll._counter
        self.head = self._dll.head
        self.tail = self._dll.tail

    def __len__(self):
        """Overwrite Python built in len function."""
        return self.counter

    def length(self):
        """Will use DLL counter for length."""
        return self._dll._counter

    def enqueue(self, data):
        """Add node to queue at head."""
        self._dll.push(data)

    def dequeue(self):
        """Remove node from queue at tail."""
        return self._dll.shift()

    def peek(self):
        """Display a value without removing it."""
        if self.length == 0:
            return None
        return self._dll.tail.data
