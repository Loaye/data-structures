"""test for Singly linked list."""


import pytest


def test_node_has_attributes():
    """Test that Node has attributes."""
    from linked_list import Node
    n = Node(1, None)
    assert hasattr(n, 'data')
    assert hasattr(n, 'data')


def test_linked_list_has_head():
    """Test that linked list has a head."""
    from linked_list import LinkedList
    l = LinkedList()
    assert l.head is None


def test_linked_list_push_adds_new_item():
    """Test that push method add a new item to Linked list."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('val')
    l.push('val2')
    assert l.head.data == 'val2'


def test_linked_list_push_two_new_item():
    """Test that push method adds 2 new items to linked list."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('val')
    l.push('val2')
    assert l.head.data == 'val2'


def test_linked_list_push_moves_old_head_to_new_heads_next():
    """Test that push method properly reassigns head to head node."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('val')
    l.push('val2')
    assert l.head.next.data == 'val'


def test_linked_list_pop_removes_head_and_returns_value():
    """Test that pop method removes the head and returns its value."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('potato')
    l.pop()
    assert l.head is None


def test_linked_list_returns_head_value():
    """Test that pop returns the head vaule."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('potato')
    assert l.pop() == ('potato')


def test_linked_list_pop_shifts_head_properly():
    """Test that pop method reassigns head to new node."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('potato')
    l.push('cabbage')
    l.pop()
    assert l.head.data == 'potato'


def test_linked_list_pop_empty_raises_exception():
    """Test that pop on empty list raises exception."""
    from linked_list import LinkedList
    l = LinkedList()
    with pytest.raises(IndexError):
        l.pop()


def test_linked_list_size_returns_list_length():
    """Test that size method returns proper list length."""
    from linked_list import LinkedList
    l = LinkedList()
    assert l.size() == 0


@pytest.mark.parametrize('n', range(100))
def test_linked_list_size_returns_list_length2(n):
    """Test that size method returns proper length from a random list."""
    from linked_list import LinkedList
    l = LinkedList()
    for i in range(n):
        l.push(i)
    assert l.size() == n


def test_linked_list_search_empty_returns_none():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push(1)
    assert l.search(4) is None


def test_linked_list_search_returns_with_one_return_node():
    """Test that search method will return as stated."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push(1)
    assert l.search(1) == l.head


def test_linked_list_search__with_one_bad_search():
    """Test that search method returns none if not found."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push(1)
    assert l.search(0) is None


@pytest.mark.parametrize('n', range(1, 10))
def test_linked_list_search__with_one_bad_search2(n):
    """Test that checks the search method for a bad value."""
    from linked_list import LinkedList
    from random import randint
    l = LinkedList()
    for i in range(1, n + 1):
        l.push(i)
    search_me = randint(1, n)
    assert l.search(search_me).data == search_me


# def test_linked_list_can_take_iterable():
#     """."""
#     from linked_list import LinkedList
#     a_list = [4, 3, 2, 6, 4, 9, 8]
#     l = LinkedList(a_list)
#     for item in a_list:
#         pass  # assert l.search(item).data == item


# def test_linked_list_display():
#     """."""
#     from linked_list import LinkedList
#     a_list = [4, 3, 2, 6, 4, 9, 8]
#     new_list = LinkedList(a_list)
#     assert new_list.display() == ('1', '8', '9', '4', '6', '2', '3')
