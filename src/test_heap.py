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

def test_bheap_pops_value(empty_heap):
    """."""
    empty_heap.push(5)
    empty_heap.pop()
    assert bheap.pop.data = 5

def test_when_pop_is_called_on_empty_heap_raise_error(empty_heap):
    """Raises an error when pop is called on an empty heap."""
    with pytest.raises(IndexError):
        empty_heap.pop()


# empty heap raise error
# identify parent and child
# error if value is not unique
# given an input of numbers - heap sorts
# heap take iterable - throws error if not iterable
# test sorts after pop
    
# def test_heap_pop_always_sorted_order():
#     """."""
#     from heap import BinaryHeap
#     import random
#     random_nums = list(set([random.randint(0, 1000) for i in range(10)]))
#     heap = BinaryHeap(random_nums)
#     all_popped = [heap.pop() for i in range(heap._size)]
#     assert all_popped == sorted(random_nums, reverse=True)
