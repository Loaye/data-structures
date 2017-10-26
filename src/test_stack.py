"""Test for the stack."""

import pytest


def test_stack_push_adds_new_item():
    """Pushing creates a new head."""
    from stack import Stack
    s = Stack()
    s.push('val')
    assert s.head.data == 'val'


def test_stack_pop_removes_head_and_returns_value():
    """Pop removes head."""
    from stack import Stack
    s = Stack()
    s.push('potato')
    s.pop()
    assert s.head is None


def test_len_function_returns_counter():
    """Len will work as intended."""
    from stack import Stack
    s = Stack()
    s.push('potato')
    s.push("beans")
    assert len(s) == 2

def test_using_list_to_instantiate():
    """Object constructor can use a list"""
    from stack import Stack
    values = [1, 2, 3]
    s = Stack(values)
    assert s.head.data == 3