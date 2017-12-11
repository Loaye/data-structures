"""Test file for bubble sort."""
import pytest


def test_bubble_sort_does_not_accept_string():
    """Test if value error raised if str passed in func."""
    from bubble_sort import bubble_sort
    with pytest.raises(TypeError):
        bubble_sort('5, 12, 3, 7')