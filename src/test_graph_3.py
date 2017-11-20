"""Test for graph_3"""
import pytest


def test_graph_initialization():
    """Create graph."""
    from graph_3 import Graph
    new_graph = Graph()
    assert isinstance(new_graph.nodes, dict)


def test_graph_add_node():
    """Add a node."""
    from graph_3 import Graph
    new_graph = Graph()
    new_graph.add_node(5)
    assert 5 in new_graph.nodes


def test_graph_add_dupe_node():
    """New node to graph."""
    from graph_3 import Graph
    new_graph = Graph()
    new_graph.add_node(5)
    with pytest.raises(ValueError):
        new_graph.add_node(5)


def test_graph_add_edge():
    """Test edge with distance."""
    from graph_3 import Graph
    new_graph = Graph()
    new_graph.add_edge('A', 'B', 5)
    assert new_graph.nodes == {'A': {'B': 5}, 'B': {}}


def test_delete_edge():
    """Test if deleting edge removes edge and distance associated wit it."""
    from graph_3 import Graph
    new_graph = Graph()
    new_graph.add_edge(5, 10, 15)
    new_graph.del_edge(5, 10)
    assert new_graph.nodes == {5: {}, 10: {}}