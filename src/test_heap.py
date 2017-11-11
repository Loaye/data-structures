"""Test heap module."""


import pytest


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
    assert bheap.heap.data == bheap.heap.data[3]


<<<<<<< HEAD
=======
def test_pop_removes_node_returns_value():
    """Test that pop removes a node and returns its value."""
    from heap import BinaryHeap
    bheap = BinaryHeap()
    bheap.append(3)
    assert bheap.heap.pop() == 3


def test_swap_properly_resorts_nodes():
    """."""
    pass

def test_float_up_moves_the_child_above_the_parent_if_the_value_is_greater():
    """."""
    pass

def test_bubbledown_
    """."""
    pass

>>>>>>> 4d8bf110d3f7af065888e9ea3312847e0adba7f9
# def test_heap_pop_always_sorted_order():
#     """."""
#     from heap import BinaryHeap
#     import random
#     random_nums = list(set([random.randint(0, 1000) for i in range(10)]))
#     heap = BinaryHeap(random_nums)
#     all_popped = [heap.pop() for i in range(heap._size)]
#     assert all_popped == sorted(random_nums, reverse=True)
