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

    def __len__(self):
        """Will work with the len() function to find length of the DLL."""
        return self._counter

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
        """Removes a given Node value from the end/tail of the list"""
        if not self.tail:
            raise IndexError("The List is empty, so there is nothing to shift/remove.")
        output = self.tail.data
        self.tail = self.tail.prev
        self._counter -= 1
        return output

    def remove(self, val):
        """Search for a given node value and remove it."""
        
        curr = self.head

        if self.head == val:
            pop()

        if self.tail == val:
            shift()

        while curr:
            if curr.data == val:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                self._counter -= 1
                return curr
            else:
                curr = curr.next

        raise ValueError("Node not in current List")