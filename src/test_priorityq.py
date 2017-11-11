"""Test for priorityq"""

import pytest


def test_initialization_empty_dict():
    """Test if to see if created."""
    from priorityq import PriorityQueue
    new_priq = PriorityQueue()
    assert new_priq.pq_dict == {}


def test_inserts_value_no_priority():
    """Test if insert."""
    from priorityq import PriorityQueue
    new_priq = PriorityQueue()
    new_priq.insert(50)
    assert new_priq.pq_dict == {0: [50]}

def test_inserts_two_diff_priorities(priq):
    """Test inserting two values with different priorities."""
    priq.insert(6, 1)
    priq.insert(44, 2)
    assert priq.pq_dict == {1: [6], 2: [44]}


def test_inserts_two_val_same_pri(priq):
    """Test inserting two values with same priorities."""
    priq.insert(6, 1)
    priq.insert(44, 1)
    assert priq.pq_dict == {1: [6, 44]}


def test_pop_empty_priq(priq):
    """Test popping on empty priq."""
    with pytest.raises(IndexError):
        priq.pop()

def test_peek_at_empty_priq(priq):
    """Test peek method when priq is empty."""
    with pytest.raises(IndexError):
        priq.peek()