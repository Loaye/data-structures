"""Sets fixtures for DSA tests"""
import pytest

@pytest.fixture
def dll_empty():
    """Fixture #1 for creating an empty dll."""
    from dll import DoublyLinkedList
    return DoublyLinkedList()

@pytest.fixture
def dll_three_nodes():
    """Fixture #2 for creating a dll with 3 nodes."""
    from dll import DoublyLinkedList
    d = DoublyLinkedList
    d.data.push(5)
    d.push(10)
    d.push(15)
    return d

@pytest.fixture
def priq():
    """Fixture #3 for creating an empty priq."""
    from priorityq import PriorityQueue
    new_priq = PriorityQueue()
    return new_priq
