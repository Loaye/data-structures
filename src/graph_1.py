"""Use of a graph."""

class Graph:
    """Implement a graph."""

    def __init__(self):
        """Instantiate a graph"""
        self.graph = {}

    def add_node(self, *args):
        """Add a new node to the graph"""
        for data in arg:
            self.graph.setdefault(data, [])

    def add_edge(self, data_1, data_2):
        """Add a edge between nodes"""
        self.add_node(data_1, data_2)
        self.graph[data_1].append(data_2)
