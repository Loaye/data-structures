"""Test heap module."""


import pytest


@pytest.fixture
def empty_heap():
    """Create an empty heap."""
    from heap import BinaryHeap
    return BinaryHeap()


def test_bin_heap_initializes_empty_list():
    """."""
    from heap import BinaryHeap
    bheap = BinaryHeap()
    assert bheap.heap == [0]


def test_push_adds_single_val_to_heap():
    """Test that push properly adds 1 value to the heap."""
    from heap import BinaryHeap
    bheap = BinaryHeap()
    bheap.push(3)


def test_bheap_pops_value(empty_heap):
    """Test that Pop function properly removes node and returns value."""
    empty_heap.push(5)
    assert empty_heap.pop() == 5


def test_when_pop_is_called_on_empty_heap_raise_error(empty_heap):
    """Raise an error when pop is called on an empty heap."""
    with pytest.raises(IndexError):
        empty_heap.pop()


def test_identify_parent_from_child(empty_heap):
    """Test that our child and parent can see each other."""
    empty_heap.push(10)
    empty_heap.push(5)
    assert empty_heap.heap[1] > empty_heap.heap[2]


def test_when_given_list_of_vals_heap_properly_sorts(empty_heap):
    """Test that if we push several values into heap, the structure is properly sorted."""
    empty_heap.push(10)
    empty_heap.push(8)
    empty_heap.push(13)
    empty_heap.push(9)
    empty_heap.push(1)
    empty_heap.push(6)
    empty_heap.push(7)
    assert empty_heap.heap == [0, 13, 9, 10, 8, 1, 6, 7]


def test_when_poping_all_vals_that_they_are_popped_in_order(empty_heap):
    """Test that when everything is popped out, it goes into a list that is properly sorted."""
    empty_heap.push(10)
    empty_heap.push(8)
    empty_heap.push(13)
    empty_heap.push(9)
    empty_heap.push(1)
    empty_heap.push(6)
    empty_heap.push(7)
    emptied_list = []
    emptied_list.append(empty_heap.pop())
    emptied_list.append(empty_heap.pop())
    emptied_list.append(empty_heap.pop())
    emptied_list.append(empty_heap.pop())
    emptied_list.append(empty_heap.pop())
    emptied_list.append(empty_heap.pop())
    emptied_list.append(empty_heap.pop())
    assert emptied_list == [13, 10, 9, 8, 7, 6, 1]
