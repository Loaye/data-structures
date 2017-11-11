"""File implements a stack with push and pop methods."""


from linked_list import LinkedList


class Stack(object):
    """Create Stack class object."""

    def __init__(self, iterable=()):
        """Init method for Stack, which is composed of LinkedList methods and attributes."""
        self._linkedlist = LinkedList(iterable)
        self.head = self._linkedlist.head
        self._length = self._linkedlist._length

    def push(self, data):
        """Push method for Stack. Adds node at head."""
        self._linkedlist.push(data)

    def pop(self):
        """Pop method for Stack. Removes node at head."""
        self._linkedlist.pop()
