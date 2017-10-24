"""Singly linked list creation."""


class Node(object):
    """Creates a node object"""

    def __init__(self, data, next):
        """Constructor for the Node object."""
        self.data = data
        self.next = next


class LinkedList(object):
    """Class for containing object called LinkedList"""

    def __init__(self, iterable=()):
        """Constructor for the Linked List object."""
        self.head = None
        self._counter = 0
        if isinstance(iterable, (str, tuple, list)):
            for item in iterable:
                self.push(item)

    def push(self):
        """Add a new value to the head of the linked list."""
        new_head = Node(val, self.head)
        self.head = new_head
        self._counter += 1

    def pop(self):
        """Remove & return the value of the head of the Linked List."""
        if not self.head:
            raise IndexError("The list is empty, so there's nothing to pop.")
        output = self.head.data
        self.head = self.head.next
        self._counter -= 1
        return output

    def size(self):
        """Return the size of our list."""
        return self._counter

    def __len__(self):
        """Works with len() function to find length of linked list"""
        return self._counter

    def search(self):
        """Searches for a given node value and returns it"""
        curr = self.head
        while curr.data == val:
            return curr
        curr = curr.next

    def remove(self):
        """Searches for a given node value and remove it from the linked list"""
        pass

    def display(self):
        """Will return a unicode string representing the list as if it were a Python tuple literal: “(12, ‘sam’, 37, ‘tango’)”
"""
        pass
