"""Create our first deque. Which can push and pull from the head or tail."""


class Node(object):
    """this creates a node object that will be used for our deque."""

    def __init__(self, val):
        """Constructor for the deque project."""
        self.val = val
        self.prev = None
        self.next_node = None


class Deque(object):
    """The class for containing an object called Deque."""

    def __init__(self):
        """Constructor for the deque."""
        self.head = None
        self.tail = None
        self._counter = 0
        self.is_empty = True

    def append(self, val):
        """Function adds value the end of the deque."""
        curr = Node(val)
        self.tail = curr.prev.next_node
        self._counter += 1

    def appendleft(self, val):
        """Function adds value the front of the deque."""
        curr = Node(val, self.head)
        self.head = curr.next_node.prev
        self._counter += 1

    def pop(self):
        """Remove a value from the end of the deque and returns it."""
        if not self.tail:
            raise IndexError("The List is empty, there's nothing to pop.")
        output = self.tail.val
        self.tail = self.tail.prev
        self._counter -= 1
        return output

    def popleft(self):
        """Remove a value from the front of the deque and returns it."""
        if not self.head:
            raise IndexError("The List is empty, there's nothing to pop.")
        output = self.head.val
        self.head = self.head.next_node
        self._counter -= 1
        return output

    def peek(self):
        """Return the next value that would be returned by pop but leaves the value in the deque."""
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
