"""Test for Graph Traversal."""


import pytest


@pytest.fixture
def test_graph():
    """Create a graph with nodes and edges."""
    from graph_jake import Graph
    new_graph = Graph()
    new_graph.add_node(43)
    new_graph.add_node(34)
    new_graph.add_node(13, 31)
    new_graph.add_edge(12, 21)
    new_graph.add_edge(23, 32)
    new_graph.add_edge(5, 8)
    new_graph.add_edge(8, 16)
    return new_graph


@pytest.fixture
def looped_graph():
    """Create graph with node connected to itself."""
    from graph_jake import Graph
    new_graph = Graph()
    new_graph.add_edge(2, 2)
    return new_graph


def test_depth_first_function(test_graph):
    """Test the function provides the proper output order."""
    from graph_2 import depth_first
    df = depth_first()
    assert df(test_graph, 5) == [5, 8, 12, 13, 16, 23, 32, 34, 43]


def test_breadth_first_function(test_graph):
    """Test the function provides the proper output order."""
    from graph_2 import breadth_first
    bf = breadth_first()
    assert bf(test_graph, 5) == [5, 8, 12, 13, 16, 23, 32, 34, 43]


def test_depth_first_on_looped_graph(looped_graph):
    """Test depth first on looping graph doesn't get stuck."""
    from graph_2 import depth_first
    df = depth_first()
    df.add_edge(5, 5)
    return df
    assert df(looped_graph, 5) == [5]


def test_breadth_first_on_looped_graph(looped_graph):
    """Test breadth first on looping graph doesn't get stuck."""
    from graph_2 import breadth_first
    bf = breadth_first()
    bf.add_edge(5, 5)
    return bf
    assert bf(looped_graph, 5) == [5]
