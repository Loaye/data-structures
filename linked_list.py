"""."""


class Node(object):
    """."""

    def __init__(self, val, next=None):
         """Create a new instantiation of a node."""
        self.val = val
        self.next = next


    def get_data(self):
        return self.val

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList(object):
    """."""

    def __init__(self, head=None):
        """."""
        self.head = head


    def push(self, val):
        """."""
        new Node(val)
        node.next = head


    def remove(self, val)


def search(self, val)

def display()

def pop()

# next=None