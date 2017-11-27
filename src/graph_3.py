"""Graph with weight edges."""


class Graph(object):
    """Create Graph class."""

    def __init__(self):
        """Create a node class."""
        self.nodes = dict()

    def add_node(self, val):
        """Add a node"""
        if val in self.nodes:
            raise ValueError('Duplicates not allowed.')
        self.nodes[val] = dict()

    def add_edge(self, val1, val2, dist):
        """Makes a bridge between 2 nodes."""
        if val1 not in self.nodes:
            self.add_node(val1)
        if val2 not in self.nodes:
            self.add_node(val2)
        if val2 in self.nodes[val1]:
            print('Edge already exists')
        self.nodes[val1][val2] = dist

    def del_node(self, val):
        """Remove a given node."""
        if val in self.nodes:
            del self.nodes[val]
        else:
            raise KeyError('Node not found.')

    def del_edge(self, val1, val2):
        """Remove an edge between 2 nodes.."""
        if val2 in self.nodes[val1]:
            del self.nodes[val1][val2]
        else:
            raise KeyError('Edge not found.')

    def has_node(self, val):
        """Check to see if node exists."""
        return True if val in self.nodes else False

    def neighbors(self, val):
        """Shows connected nodes to a given value."""
        if val in self.nodes:
            return list(self.nodes[val])
        else:
            raise KeyError('Node not found.')

    def adjacent(self, val1, val2):
        """Return True if nodes passed are connected."""
        if val1 not in self.nodes or val2 not in self.nodes:
            raise KeyError('Node not found')
        elif val2 in self.nodes[val1] or val1 in self.nodes[val2]:
            return True
        else:
            return False