"""Doubly linked list creation."""


class Node(object):
    """."""

    def __init__(self, data, next, prev):
        """."""
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList(object):
    """."""

    def __init__(self, iterable=[]):
        """."""
        self.head = None
        self.tail = None
        self._counter = 0
        if isinstance(iterable, (str, tuple, list)):
            for item in iterable:
                self.push(item)

    def push(self, val):
        """."""

    def append(self, val):
        """."""

    def pop(self):
        """."""

    def shift(self):
        """."""

    def remove(self, val):
        """."""

    def size(self):
        """."""
