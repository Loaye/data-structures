"""test for Doubly linked list."""


import pytest


def test_node_has_attributes():
    """Test that Node has attributes."""
    from dll import Node
    n = Node(1, None)
    assert hasattr(n, 'data')
    assert hasattr(n, 'data')


def test_dll_has_head():
    """Test that dll has a head."""
    from dll import DoublyLinkedList
    l = DoublyLinkedList()
    assert l.head is None


def test_dll_has_tail():
    """Test that dll has a head."""
    from dll import DoublyLinkedList
    l = DoublyLinkedList()
    assert l.tail is None


def test_counter():
    """"Test that counter properly adds and removes proper amount of nodes."""
    from dll import DoublyLinkedList
    l = DoublyLinkedList()
    assert l._counter is None


def test_dll_can_take_iterable():
    """Test to see that list can take a list or tuple."""
    from dll import DoublyLinkedList
    a_list = [4, 3, 2, 6, 4, 9, 8]
    l = DoublyLinkedList(a_list)
    for item in a_list:
        assert l.search(item).data == item


def test_len_process():
    """."""


def test_dll_push_adds_new_item():
    """Test that push method add a new item to Linked list."""
    from dll import push
    l = dll()
    l.push('val')
    l.push('val2')
    assert l.head.data == 'val2'


def test_dll_push_two_new_item():
    """Test that push method adds 2 new items to linked list."""
    from dll import push
    l = dll()
    l.push('val')
    l.push('val2')
    assert l.head.data == 'val2'


def test_dll_push_moves_old_head_to_new_heads_next():
    """Test that push method properly reassigns head to head node."""
    from dll import push
    l = dll()
    l.push('val')
    l.push('val2')
    assert l.head.next.data == 'val'


def test_append():
    """Test that push method properly reassigns head to head node."""
    from dll import append
    l = dll()


def test_dll_pop_removes_head_and_returns_value():
    """Test that pop method removes the head and returns its value."""
    from dll import pop
    l = dll()
    l.push('potato')
    l.pop()
    assert l.head is None
