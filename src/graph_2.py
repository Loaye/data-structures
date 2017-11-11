"""Graph Traversal of nodes and edges."""


from graph_jake import Graph


def depth_first(graph, node):
    """Traverse the graph depth-first."""
    visited = []

    def traverse(graph, node):
        layer = []
        visited.append(node)
        layer.append(node)
        node = graph.nodes[node]
        for val in node:
            if val not in visited:
                layer.extend(traverse(graph, val))
        return layer
    return traverse(graph, node)


def breadth_first(graph, node):
    """Traverse the graph breadth-first."""
    visited = []
    route = [node]
    while route:
        current = route.pop(0)
        if current not in visited:
            visited.append(current)
            route.extend(graph.nodes[current])
    return visited


if __name__ == '__main__':
    g = Graph()
    g.add_edge(1, 4)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(2, 3)
    g.add_edge(1, 3)
    g.add_edge(1, 5)
    g.add_edge(2, 6)
    g.add_edge(3, 6)
    g.add_edge(1, 6)
    print(g.nodes)
    print(depth_first(g, 1))
    print(breadth_first(g, 1))
