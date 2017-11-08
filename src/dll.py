"""Doubly linked list creation."""


class Node(object):
    """This creates a node object."""

    def __init__(self, data, next_node=None, prev=None):
        """Constructor for the Node object."""
        self.data = data
        self.next_node = next_node
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

    def push(self, data):
        """Add a new value to the head of the linked list."""
        curr = Node(data)
        if self.head is None:
            self.head = curr
            self.tail = curr
        else:
            self.head.prev = curr
            curr.next_node = self.head
            self.head = curr
        self._counter += 1

    def append(self, data):
        """Add a node to the end/tail side of the DLL."""
        curr = Node(data)
        if self.tail is None:
            self.head = curr
            self.tail = curr
        else:
            self.tail.next_node = curr
            curr.prev = self.tail
            self.tail = curr
        self._counter += 1

    def pop(self):
        """Remove & return the value of the head of the DLL."""
        if not self.head:
            raise IndexError("The List is empty, so there's nothing to pop.")
        output = self.head.data
        self.head = self.head.next_node
        self._counter -= 1
        return output

    def shift(self):
        """Remove a given Node value from the end/tail of the list."""
        if not self.tail:
            raise IndexError("The List is empty, there is nothing to shift.")
        output = self.tail.data
        self.tail = self.tail.prev
        self.tail.next_node = None
        self._counter -= 1
        return output

    def remove(self, val):
        """Search for a given node value and remove it."""
        curr = self.head
        curr.prev = None

        while curr:
            if curr.data == val:
                if self.head == self.tail:
                    self.head = self.tail = None
                    self._counter -= 1
                    return
                if curr == self.tail:
                    self.tail.next_node = None
                    curr.prev = None
                    self._counter -= 1
                    return
                if prev:
                    prev.next_node = curr.next_node
                    curr.next_node.prev = curr.prev
                    curr.next_node = curr.prev = None
                    self._counter -= 1
                    return
                else:
                    curr.next_node.prev = curr.next_node = None
                    self._counter -= 1
                    return
            prev = curr
            curr = prev.next_node
        raise ValueError("Node not in current List")

    def display(self):
        """Return a unicode string that represents the list as a tuple."""
        curr = self.head
        make_tuple = "("
        while curr:
            make_tuple += str(curr.data) + ", "
            curr = curr.next_node
        make_tuple = make_tuple[:-2]
        make_tuple += ")"
        return make_tuple

    def size(self):
        """Return the size of the dll."""
        return self._counter
