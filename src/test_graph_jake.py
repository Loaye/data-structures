"""Test file for graph.py."""
import pytest


def test_graph_initialization():
    """Test creation of graph object."""
    from graph import Graph
    new_graph = Graph()
    assert isinstance(new_graph.nodes, dict)

def test_graph_add_node():
    """Test adding a new node to empty graph."""
    from graph import Graph
    new_graph = Graph()
    new_graph.add_node(9)
    assert 9 in new_graph.nodes

def test_graph_add_dupe_node():
    """Test adding a new node to empty graph."""
    from graph import Graph
    new_graph = Graph()
    new_graph.add_node(9)
    with pytest.raises(ValueError):
        new_graph.add_node(9)

def test_graph_add_second_node(graph_1):
    """Test adding a second node to graph."""
    graph_1.add_node(2)
    assert isinstance(graph_1.nodes[2], set)

def test_add_edge_one_existing_node(graph_1):
    """Test adding an edge between one existing node, and one that hasn't been created yet."""
    graph_1.add_edge(5, 9)
    assert graph_1.nodes[5] == {9}

def test_del_edge_removes_val(graph_w_edge):
    """Test del_edge to ensure val removed from associated key."""
    graph_w_edge.del_edge(84, 2)
    assert graph_w_edge.nodes[84] == set()


def test_del_edge_raise_error_no_edge(graph_w_edge):
    """Test to raise edge not found KeyError."""
    with pytest.raises(KeyError):
        graph_w_edge.del_edge(84, 9)

def test_has_node_true_after_del_edge(graph_w_edge):
    """Test that has_node is True after edge deleted."""
    graph_w_edge.del_edge(84, 2)
    assert graph_w_edge.has_node(2) is True


def test_neighbors(graph_w_edge):
    """Test neighbors returns list of connected nodes."""
    graph_w_edge.add_edge(84, 17)
    assert 17 in graph_w_edge.neighbors(84)
    assert 2 in graph_w_edge.neighbors(84)

def test_neighbors_key_error(graph_w_edge):
    """Test KeyError raises calling neighbor with invalid node."""
    with pytest.raises(KeyError):
        graph_w_edge.neighbors(112)

def test_adjacent_val_connected(graph_w_edge):
    """Test True if values are connected."""
    assert graph_w_edge.adjacent(2, 84) is True

def test_edge_deleted_if_node_deleted(graph_w_edge):
    """Test if that edge is deleted if node is deleted."""
    graph_w_edge.del_node(2)
    assert 2 not in graph_w_edge.nodes[84]
