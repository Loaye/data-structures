"""File implements a stack with push and pop methods."""


from linked_list import LinkedList


class Stack(object):
    """Create Stack class object."""

    def __init__(self, iterable=()):
<<<<<<< HEAD
        """Init method for Stack.  Stack is composed of LinkedList methods and attributes."""
=======
<<<<<<< HEAD
        """Init method for Stack, which is composed of LinkedList methods and attributes."""
=======
        """Init method for Stack.  Stack is composed of LinkedList methods and attributes."""
>>>>>>> master
>>>>>>> 10f611599dd85ea275019f2a7502d2fdd09901c4
        self._linkedlist = LinkedList(iterable)
        self.head = self._linkedlist.head
        self._length = self._linkedlist._length

    def push(self, data):
        """Push method for Stack. Adds node at head."""
        self._linkedlist.push(data)

    def pop(self):
        """Pop method for Stack. Removes node at head."""
        self._linkedlist.pop()
