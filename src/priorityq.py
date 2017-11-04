"""Implementation of a priority que"""

class PriorityQueue(object):
    """Initialize of PriorityQueue class."""
    self.pq_dict = {}

    def insert(self, data, priority=0):
        "Add value to queue with data and optional"
        if not isisntace(data, (int, float)):
            raise TypeError('Must be a number, try again')
        if priority in self.pq_dict:
            self.pq_dict[priority].append(data)

    def pop(self):
        """Removes a value in priority order."""
        if self.pq_dict == {}:
            raise IndexError('Empty Queue')
        highest_p = max(self.pq_dict)
        delete_val = self.pq_dict[highest_p][0]
        del self.pq_dict[highest_p][0]
        if len(self.pq_dict[highest_p]) == 0:
            del self.pq_dict[highest_p]
        return delete_val

    def peek(self):
        """Returns the highest priorty without deleting it."""
        if self.pq_dict == {}:
            raise IndentationError("Empty Queue")
        highest_p = max(self.pq_dict)
        peek_val = self.pq_dict[highest_p][0]
        return peek_val