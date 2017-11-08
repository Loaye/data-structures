"""Test for Doubly linked list."""


import pytest


@pytest.fixture
def dll_empty():
    """Set up out empty dll for testing."""
    from dll import DoublyLinkedList
    return DoublyLinkedList()


@pytest.fixture
def dll_three_nodes():
    """Set up the fixture process used for testing."""
    from dll import DoublyLinkedList
    d = DoublyLinkedList()
    d.push(5)
    d.push(10)
    d.push(15)
    return d


def test_node_object_exists():
    """Test that the Node Class is working."""
    from dll import Node
    node = Node(3)
    assert node


def test_search_found(dll_empty):
    """Test that search will find the given node value in the DLL."""
    dll_empty.push(20)
    assert dll_empty.search(20)


def test_size_after_tail_has_been_removed(dll_three_nodes):
    """Test the size of the dll after a tail has been removed."""
    dll_three_nodes.remove(5)
    assert dll_three_nodes.size() == 2


def test_append_adds_value_to_tail(dll_empty):
    """Test that appended value is the tail."""
    dll_empty.append(1)
    assert dll_empty.tail.data == 1

    
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


def test_dll_push_adds_new_item():
    """Test that push method add a new item to Linked list."""
    from dll import DoublyLinkedList
    l = DoublyLinkedList()
    l.push('val')
    l.push('val2')
    assert l.head.data == 'val2'

   
def test_push_to_empty_adds_value_to_head(dll_empty):
    """Test that the pushed node gives value to head."""
    dll_empty.push(1)
    assert dll_empty.head.data == 1


def test_push_to_empty_sets_head_and_tail(dll_empty):
    """Test to push empty."""
    dll_empty.push(1)
    assert dll_empty.head is dll_empty.tail


def test_dll_push_two_new_item():
    """Test that push method adds 2 new items to linked list."""
    from dll import DoublyLinkedList
    l = DoublyLinkedList()
    l.push('val')
    l.push('val2')
    assert l.head.data == 'val2'


def test_dll_push_moves_old_head_to_new_heads_next():
    """Test that push method properly reassigns head to head node."""
    from dll import DoublyLinkedList
    l = DoublyLinkedList()
    l.push('val')
    l.push('val2')
    assert l.head.next.data == 'val'


def test_append_adds_value_to_tail(dll_empty):
    """Test that appended value is the tail."""
    dll_empty.append(1)
    assert dll_empty.tail == dll_empty.tail.data


def test_append_multiple_vals_to_tail(dll_empty):
    """Test that last value appended is the tail."""
    dll_empty.append(1)
    dll_empty.append(5)
    dll_empty.append(9)
    assert dll_empty.tail.data == 9


def test_dll_pop_removes_head_and_returns_value():
    """Test that pop method removes the head and returns its value."""
    from dll import DoublyLinkedList
    l = DoublyLinkedList()
    l.push('potato')
    l.pop()
    assert l.head is None


def test_display_empty_dll(dll_empty):
    """Test will display empty."""
    assert dll_empty.display() == "()"


def test_display_filled_dll():
    """Test to show the the values of all nodes."""
    from dll import DoublyLinkedList
    dll_empty = DoublyLinkedList()
    dll_empty.append(5)
    dll_empty.append(10)
    dll_empty.append(15)
    assert dll_empty.display() == "(5, 10, 15)"
