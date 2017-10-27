"""Doubly linked list creation."""


class Node(object):
    """This creates a node object."""

    def __init__(self, data, next, prev):
        """Constructor for the Node object."""
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList(object):
    """The class for containing an object called DoublyLinkedList."""

    def __init__(self, iterable=[]):
        """Constructor for the Doubly Linked List object."""
        self.head = None
        self.tail = None
        self._counter = 0
        if isinstance(iterable, (str, tuple, list)):
            for item in iterable:
                self.push(item)

    def push(self, val):
        """Add a new value to the head of the linked list."""
        curr = Node(val, self.head)
        self.head = curr.next.prev
        self._counter += 1

    def append(self, val):
        """Adds a node to the end/tail side of the DLL"""
        curr = Node(val, self.tail)
        self.tail = curr.prev.next
        self._counter += 1

    def pop(self):
        """Remove & return the value of the head of the DLL."""
        if not self.head:
            raise IndexError("The List is empty, so there's nothing to pop.")
        output = self.head.data
        self.head = self.head.next
        self._counter -= 1
        return output

    def shift(self):
        """."""

    def remove(self, val):
        """Search for a given node value and remove it."""
        # curr = self.head
        # while curr:
        #     if curr.next == node:
        #         curr.next = curr.next.next
        #     curr = curr.next
        # return curr

    def size(self):
        """Return the size of our list."""
        # return self._counter

    def __len__(self):
        """Will work with the len() function to find length of the DLL."""
        # return self.counter
