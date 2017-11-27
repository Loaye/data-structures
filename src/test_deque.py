"""Tests for deque.py."""


import pytest


def test_deque_initializes_properly():
    """Test that deque properly created."""
    from deque import Deque
    d = Deque()
    assert d


def test_deque_appends_one_value():
    """Test that deque adds one value."""
    from deque import Deque
    d = Deque()
    d.append(2)
    assert d._counter == 1


def test_appendleft_add_one_value():
    """Test that appendleft adds one value."""
    from deque import Deque
    d = Deque()
    d.appendleft(4)
    assert d._counter == 1


def test_deque_appends_one_value_on_the_end():
    """Test that append adds one value on the end."""
    from deque import Deque
    d = Deque()
    d.append(6)
    assert d.tail.val == 6


def test_appendleft_add_one_value_on_the_front():
    """Test that appendleft adds one value on the front."""
    from deque import Deque
    d = Deque()
    d.appendleft(8)
    assert d.head.val == 8


def test_deque_appends_two_valus_on_the_end():
    """Test that append adds two values on the end."""
    from deque import Deque
    d = Deque()
    d.append(6)
    d.append(8)
    assert d.tail.val == 8


def test_appendleft_adds_two_values_on_the_front():
    """Test that append adds two values on the front.""">>>>>>> cc48ed5933edacc4c37aac91c010335c453a5ee0
    from deque import Deque
    d = Deque()
    d.appendleft(6)
    d.appendleft(8)
    assert d.head.val == 8


def test_pop_removes_val_from_end_of_deque():
    """Test that pop removes a node from the end of the list and returns the value."""
    from deque import Deque
    d = Deque()
    d.append(2)
    d.append(4)
    d.append(6)
    d.append(8)
    d.pop()
    assert d.tail.val is 6


def test_popleft_removes_val_from_end_of_deque():
    """Test that pop removes a node from the front of the list and returns the value."""
    from deque import Deque
    d = Deque()
    d.append(2)
    d.append(4)
    d.append(6)
    d.append(8)
    d.popleft()
    assert d.head.val is 4


def test_peek_returns_val_from_front_of_deque():
    """Test that peek returns the value from the end but does not alter its node."""
    from deque import Deque
    d = Deque()
    d.append(2)
    d.append(4)
    d.append(6)
    d.append(8)
    assert d.peekleft() == 2


def test_peekleft_returns_val_from_end_of_deque():
    """Test that peek returns the value from the front but does not alter its node."""
    from deque import Deque
    d = Deque()
    d.append(2)
    d.append(4)
    d.append(6)
    d.append(8)
    assert d.peek() == 8
