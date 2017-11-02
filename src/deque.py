"""Create our first deque. Which can push and pull from the head or tail."""


class Node(object):
    """this creates a node object that will be used for our deque."""

    def __init__(self, val, prev=None, next_node=None):
        """Constructor for the deque project."""
        self.val = val
        self.prev = prev
        self.next_node = next_node


class Deque(object):
    """The class for containing an object called Deque."""

    def __init__(self):
        """Constructor for the deque."""
        self.head = None
        self.tail = None
        self._counter = 0

    def append(self, val):
        """Function adds value the end of the deque."""
        curr = Node(val, prev=self.tail)
        if self._counter == 0:
            self.tail = curr
            self.head = curr
        self.tail.next_node = curr
        self.tail = curr
        self._counter += 1

    def appendleft(self, val):
        """Function adds value the front of the deque."""
        curr = Node(val, next_node=self.head)
        if self._counter == 0:
            self.tail = curr
            self.head = curr
        self.head.prev = curr
        self.head = curr
        self._counter += 1

    def pop(self):
        """Remove a value from the end of the deque and returns it."""
        if not self.tail:
            raise IndexError("The List is empty, there's nothing to pop.")
        output = self.tail.val
        self.tail = self.tail.prev
        self.tail.next_node = None
        self._counter -= 1
        return output

    def popleft(self):
        """Remove a value from the front of the deque and returns it."""
        if not self.head:
            raise IndexError("The List is empty, there's nothing to pop.")
        output = self.head.val
        self.head = self.head.next_node
        self.head.prev = None
        self._counter -= 1
        return output

    def peek(self):
        """Return the next value that would be returned by pop but leaves thevalue in the deque."""
        if not self.tail.val:
            raise IndexError("The List is empty, there's nothing to see.")
        return self.tail.val

    def peekleft(self):
        """Return the next value that would be returned by popleft but leaves the value in the deque."""
        if not self.head.val:
            raise IndexError("The List is empty, there's nothing to see.")
        return self.head.val

    def size(self):
        """Return the count of items in the queue."""
        return self._counter
