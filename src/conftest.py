"""Sets fixtures for DSA tests"""
import pytest

@pytest.fixture
def dll_empty():
    """."""
    from dll import DoublyLinkedList
    return DoublyLinkedList()

@pytest.fixture
def dll_three_nodes():
    """."""
    from dll import DoublyLinkedList
    d = DoublyLinkedList
    d.data.push(5)
    d.push(10)
    d.push(15)
    return d
