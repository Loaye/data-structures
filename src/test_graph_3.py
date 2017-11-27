"""Test file for dijkstra."""
import pytest

def test_4_nodes_dist():
    """."""
    import pytest
    from djs_algorithm import djs_algorithm 
    nodelist = ['a', 'b', 'c', 'd']
    edges = {('a', 'c'): 10,
             ('a', 'b'): 6,
             ('b', 'd'): 2,
             ('c', 'd'): 6,
             }
    dist, route = djs_algorithm('a', 'd', nodelist, edges)
    assert dist == 6


def test_4_nodes_list():
    """."""
    from graph_3 import Graph 
    import pytest
    nodelist = ['a', 'b', 'c', 'd']
    edges = {('a', 'c'): ,
             ('a', 'b'): 6,
             ('b', 'd'): 2,
             ('c', 'd'): 6,
             }
    dist, route = Graph('a', 'd', nodelist, edges)
    assert route == ['a', 'b', 'd']


def test_4_nodes_list02():
    """."""
    from graph_3 import Graph 
    import pytest
    nodelist = ['a', 'b', 'c', 'd']
    edges = {('a', 'c'): 10,
             ('a', 'b'): 6,
             ('b', 'd'): 2,
             ('c', 'd'): 6,
             }
    dist, route = Graph('c', 'd', nodelist, edges)
    assert route == ['c', 'd']