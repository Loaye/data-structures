"""Tests for DLL"""
import pytest


def test_node_object_exists():
    """Tests that the Node Class is working"""
    from dll import Node
    node = Node(0, 1, 3)
    assert node

def test_search_found(dll_empty):
    """Test that search will find the given node value in the DLL"""
    dll_empty.push(20)
    assert dll_empty.search(20)

def test_size_after_tail_has_been_removed(dll_three_nodes):
    """Test the size of the dll after a tail has been removed"""
    dll_three_nodes.remove(5)
    assert dll_three_nodes.size() == 2

def test_append_adds_value_to_tail(dll_empty):
    """Test that appended value is the tail"""
    dll_empty.append(1)
    assert dll_empty.tail == tail.data

def test_append_multiple_vals_to_tail(dll_empty):
    """Test that last value appended is the tail."""
    dll_empty.append(1)
    dll_empty.append(5)
    dll_empty.append(9)
    assert dll_empty.tail.data == 9

def test_push_to_empty_adds_value_to_head(dll_empty):
    """Test that the pushed node gives value to head."""
    dll_empty.push(1)
    assert dll_empty.head.data == 1

def test_push_to_empty_sets_head_and_tail(dll_empty):
    """Test to push empty."""
    dll_empty.push(1)
    assert dll_empty.head is dll_empty.tail

def test_display_empty_dll(dll_empty):
    """Test will display empty."""
    assert dll_empty.display() == "()"

def test_display_filled_dll(dll_empty):
    """Test to show the the values of ."""
    dll_empty.append(5)
    dll_empty.append(10)
    dll_empty.append(15)
    assert dll_three_nodes.display() == "(5, 10, 15)"
