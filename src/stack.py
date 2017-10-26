"""Creates a stack - a subset of Linked List."""
from linked_list_code_base import LinkedList


class Stack(LinkedList):
    """Creates a Stack."""
    
    def pop(self):
        """Remove the top node and returns it's value"""
        try:
            return self._values.pop()
        except IndexError:
            raise IndexError('Can not pop from empty stack')
