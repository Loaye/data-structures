"""Test heap module."""


import pytest


def test_heap_pop_always_sorted_order():
    """."""
    from bin_heap import Heap
    import random
    random_nums = list(set([random.randint(0, 1000) for i in range(10)]))
    heap = Heap(random_nums)
    all_popped = [heap.pop() for i in range(heap._size)]
    assert all_popped == sorted(random_nums, reverse=True)
