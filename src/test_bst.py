"""Tests for Binary Search Tree."""
import pytest


def test_node_initialized():
    """Test that node object is initialized."""
    from bst import Node
    n = Node(1)
    assert n.data == 1


def test_bst_initialized(bst_empty):
    """Test new bst has no root."""
    assert bst_empty.root is None


def test_bst_three_root(bst_three):
    """Test root attributes of bst with three nodes."""
    assert bst_three.root.data == 10
    assert bst_three.root.left.data == 5
    assert bst_three.root.right.data == 15


def test_insert_duplicate_data(bst_three):
    """Test return when trying to insert data already in tree."""
    assert bst_three.insert(5) == "Duplicate data"


def test_insert_node_in_bst_three(bst_three):
    """Test node is inserted in the correct place."""
    bst_three.insert(13)
    assert bst_three.root.right.left.data == 13


def test_size_bst_three(bst_three):
    """Test size is corrent on bst with three nodes."""
    assert bst_three.size() == 3


def test_size_bst_three_insert_one(bst_three):
    """Test size is corrent on bst with three nodes after insert."""
    bst_three.insert(8)
    assert bst_three.size() == 4


def test_search_valid_data(bst_three):
    """Test search for data in tree returns correct node data."""
    assert bst_three.search(15).data == 15


def test_search_valid_data_return_node(bst_three):
    """Test search for data in tree returns correct node."""
    assert bst_three.search(5) == bst_three.root.left


def test_search_invalid_data(bst_three):
    """Test search for data not in tree returns None."""
    assert bst_three.search(22) is None


def test_search_data_in_root(bst_three):
    """Test search for data in root returns root node."""
    assert bst_three.search(10) == bst_three.root


def test_contains_data_in_tree(bst_three):
    """Test contains method on data in tree returns True."""
    assert bst_three.contains(5) is True


def test_contains_data_not_in_tree(bst_three):
    """Test contains method on data in tree returns True."""
    assert bst_three.contains(8) is False


def test_depth_of_zero_empty_tree(bst_empty):
    """Depth on empty tree is 0."""
    assert bst_empty.depth() == 0


def test_depth_of_zero_tree_with_root(bst_empty):
    """Depth on tree with one node is 0."""
    bst_empty.insert(30)
    assert bst_empty.depth() == 0


def test_depth_of_one(bst_three):
    """Test that tree returns depth of 1."""
    assert bst_three.depth() == 1


def test_depth_of_two(bst_three):
    """Test tree with depth of 2."""
    bst_three.insert(8)
    assert bst_three.depth() == 2


def test_balance_equal(bst_three):
    """Test balanced tree returns 0."""
    assert bst_three.balance() == 0


def test_balance_negative_one(bst_three):
    """Test left balanced tree returns 1."""
    bst_three.insert(6)
    assert bst_three.balance() == 1


def test_balance_plus_one(bst_three):
    """Test left balanced tree returns -1."""
    bst_three.insert(20)
    assert bst_three.balance() == -1