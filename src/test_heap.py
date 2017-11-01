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


# def test_heap_pop_always_sorted_order():
#     """."""
#     from heap import BinaryHeap
#     import random
#     random_nums = list(set([random.randint(0, 1000) for i in range(10)]))
#     heap = BinaryHeap(random_nums)
#     all_popped = [heap.pop() for i in range(heap._size)]
#     assert all_popped == sorted(random_nums, reverse=True)
