"""test for Singly linked list."""


import pytest


def test_node_has_attributes():
    """Test for Node."""
    from linked_list_code_base import Node
    n = Node(1, None)
    assert hasattr(n, 'data')
    assert hasattr(n, 'data')


def test_linked_list_has_head():
    """."""
    from linked_list_code_base import LinkedList
    l = LinkedList()
    assert l.head is None


def test_linked_list_push_adds_new_item():
    """."""
    from linked_list_code_base import LinkedList
    l = LinkedList()
    l.push('val')
    assert l.head.data == 'val'


def test_linked_list_push_two_new_item():
    """."""
    from linked_list_code_base import LinkedList
    l = LinkedList()
    l.push('val')
    l.push('val2')
    assert l.head.data == 'val2'


def test_linked_list_push_moves_old_head_to_new_heads_next():
    """."""
    from linked_list_code_base import LinkedList
    l = LinkedList()
    l.push('val')
    l.push('val2')
    assert l.head.next.data == 'val'


def test_linked_list_pop_removes_head_and_returns_value():
    """."""
    from linked_list_code_base import LinkedList
    l = LinkedList()
    l.push('potato')
    l.pop()
    assert l.head is None


def test_linked_list_returns_head_value():
    """."""
    from linked_list_code_base import LinkedList
    l = LinkedList()
    l.push('potato')
    assert l.pop() == ('potato')


def test_linked_list_pop_shifts_head_properly():
    """."""
    from linked_list_code_base import LinkedList
    l = LinkedList()
    l.push('potato')
    l.push('cabbage')
    l.pop()
    assert l.head.data == 'potato'


def test_linked_list_pop_empty_raises_exception():
    """."""
    from linked_list_code_base import LinkedList
    l = LinkedList()
    with pytest.raises(IndexError):
        l.pop()


def test_linked_list_size_returns_list_length():
    """."""
    from linked_list_code_base import LinkedList
    l = LinkedList()
    assert l.size() == 0


@pytest.mark.parametrize('n', range(100))
def test_linked_list_size_returns_list_length2(n):
    """."""
    from linked_list_code_base import LinkedList
    l = LinkedList()
    for i in range(n):
        l.push(i)
    assert l.size() == n


# def test_linked_list_search__empty_returns_none():
#     """."""
#     from linked_list_code_base import LinkedList
#     l = LinkedList()
#     l.push(1)
#     assert l.search(1) is 1


def test_linked_list_search__with_one_returns_node():
    """."""
    from linked_list_code_base import LinkedList
    l = LinkedList()
    l.push(1)
    assert l.search(1) == l.head


def test_linked_list_search__with_one_bad_search():
    """."""
    from linked_list_code_base import LinkedList
    l = LinkedList()
    l.push(1)
    assert l.search(0) is None


# @pytest.mark.parametrize('n', range(1, 10))
# def test_linked_list_search__with_one_bad_search2(n):
#     """."""
#     from linked_list_code_base import LinkedList
#     from random import randint
#     l = LinkedList()
#     for i in range(1, n + 1):
#         l.push(i)
#     search_me = randint(1, n)
#     assert l.search(search_me).data == search_me


def test_linked_list_ca_take_iterable():
    """."""
    from linked_list_code_base import LinkedList
    a_list = [4, 3, 2, 6, 4, 9, 8]
    l = LinkedList(a_list)
    for item in a_list:
        pass
        # assert l.search(item).data == item

