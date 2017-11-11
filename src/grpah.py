"""Create a Graph Data Structure."""


class Vertex:
    """Create the verticies within the graph."""

    def __init__(self, node):
        """Initialize the verts."""
        self.id = node
        self.adjacent = {}

    def add_neighbor(self, neighbor):
        """Identify verts that are neighbors."""
        self.adjacent[neighbor] = neighbor

    def get_adjacents(self):
        """Identify verts that are adjacent."""
        return self.adjacent.keys()

    def get_id(self):
        """."""
        return self.id

    def add_vertex(self, node):
        """Add a vertex to the graph."""
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.g_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        """Get one vertex."""
        if n in self.g_dict:
            return self.g_dict[n]
        else:
            return None

    def add_edge(self, start, end):
        """Add edge between to verts."""
        if start not in self.g_dict:
            self.add_vertex(start)
        if end not in self.g_dict:
            self.add_vertex(end)
        self.g_dict[start].add_neighbor(self.g_dict[end])
        self.g_dict[end].add_neighbor(self.g_dict[start])

# Working sketch of our graph.
# Vertecies: ('a')('b')('c')('d')('e')('f')
# Edges: ('a', 'b')('a', 'c')('a', 'f')('b', 'c')('b', 'd')
#        ('c', 'd')('c', 'f')('d', 'e')('e', 'f')
