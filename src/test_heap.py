"""Test heap module."""


import pytest

@pytest.fixture
def empty_heap()
    """Create an empty heap"""
    from heap import BinaryHeap
    return BinaryHeap():

def test_bin_heap_initializes_empty_list():
    """."""
    from heap import BinaryHeap
    bheap = BinaryHeap()
    assert bheap.heap == []


def test_push_adds_single_val_to_heap():
    """."""
    from heap import BinaryHeap
    bheap = BinaryHeap()
    bheap.push(3)
    assert bheap.heap.data == 3

def test_bheap_pops_value(empty_heap):
    """."""
    empty_heap.push(5)
    empty_heap.pop()
    assert bheap.pop.data = 5

# empty heap raise error
# identify parent and child
# error if value is not unique
# given an input of numbers - heap sorts
# heap take iterable - throws error if not iterable
# test sorts after pop