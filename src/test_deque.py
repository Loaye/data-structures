"""Tests for deque.py."""


import pytest


def test_deque_initializes_properly():
<<<<<<< HEAD
    """."""
=======
    """Test that deque properly created."""
>>>>>>> 4d8bf110d3f7af065888e9ea3312847e0adba7f9
    from deque import Deque
    d = Deque()
    assert d


def test_deque_appends_one_value():
<<<<<<< HEAD
    """."""
=======
    """Test that deque adds one value."""
>>>>>>> 4d8bf110d3f7af065888e9ea3312847e0adba7f9
    from deque import Deque
    d = Deque()
    d.append(2)
    assert d._counter == 1


def test_appendleft_add_one_value():
<<<<<<< HEAD
    """."""
=======
    """Test that appendleft adds one value."""
>>>>>>> 4d8bf110d3f7af065888e9ea3312847e0adba7f9
    from deque import Deque
    d = Deque()
    d.appendleft(4)
    assert d._counter == 1


def test_deque_appends_one_value_on_the_end():
<<<<<<< HEAD
    """."""
=======
    """Test that append adds one value on the end."""
>>>>>>> 4d8bf110d3f7af065888e9ea3312847e0adba7f9
    from deque import Deque
    d = Deque()
    d.append(6)
    assert d.tail.val == 6


def test_appendleft_add_one_value_on_the_front():
<<<<<<< HEAD
    """."""
=======
    """Test that appendleft adds one value on the front."""
>>>>>>> 4d8bf110d3f7af065888e9ea3312847e0adba7f9
    from deque import Deque
    d = Deque()
    d.appendleft(8)
    assert d.head.val == 8


def test_deque_appends_two_valus_on_the_end():
<<<<<<< HEAD
    """."""
=======
    """Test that append adds two values on the end."""
>>>>>>> 4d8bf110d3f7af065888e9ea3312847e0adba7f9
    from deque import Deque
    d = Deque()
    d.append(6)
    d.append(8)
    assert d.tail.val == 8


def test_appendleft_adds_two_values_on_the_front():
<<<<<<< HEAD
    """."""
=======
    """Test that append adds two values on the front."""
>>>>>>> 4d8bf110d3f7af065888e9ea3312847e0adba7f9
    from deque import Deque
    d = Deque()
    d.appendleft(6)
    d.appendleft(8)
    assert d.head.val == 8


def test_pop_removes_val_from_end_of_deque():
<<<<<<< HEAD
    """."""
=======
    """Test that pop removes a node from the end of the list and returns the value."""
>>>>>>> 4d8bf110d3f7af065888e9ea3312847e0adba7f9
    from deque import Deque
    d = Deque()
    d.append(2)
    d.append(4)
    d.append(6)
    d.append(8)
    d.pop()
    assert d.tail.val is 6


def test_popleft_removes_val_from_end_of_deque():
<<<<<<< HEAD
    """."""
=======
    """Test that pop removes a node from the front of the list and returns the value."""
>>>>>>> 4d8bf110d3f7af065888e9ea3312847e0adba7f9
    from deque import Deque
    d = Deque()
    d.append(2)
    d.append(4)
    d.append(6)
    d.append(8)
    d.popleft()
    assert d.head.val is 4


def test_peek_returns_val_from_front_of_deque():
<<<<<<< HEAD
    """."""
=======
    """Test that peek returns the value from the end but does not alter its node."""
>>>>>>> 4d8bf110d3f7af065888e9ea3312847e0adba7f9
    from deque import Deque
    d = Deque()
    d.append(2)
    d.append(4)
    d.append(6)
    d.append(8)
    assert d.peekleft() == 2


def test_peekleft_returns_val_from_end_of_deque():
<<<<<<< HEAD
    """."""
=======
    """Test that peek returns the value from the front but does not alter its node."""
>>>>>>> 4d8bf110d3f7af065888e9ea3312847e0adba7f9
    from deque import Deque
    d = Deque()
    d.append(2)
    d.append(4)
    d.append(6)
    d.append(8)
    assert d.peek() == 8
