"""Test file for Binary Search Tree (bst.py)."""
import pytest


@pytest.fixture
def bst():
    """Initialize an empty bst."""
    from bst import BinarySearchTree
    return BinarySearchTree()


@pytest.fixture
def empty_tree():
    """Empty BST fixture."""
    from bst import BinarySearchTree
    tree = BinarySearchTree()
    return tree


@pytest.fixture
def full_tree():
    """Create bst will values for tests."""
    from bst import BinarySearchTree
    test_bst = BinarySearchTree()
    test_bst.insert(6)
    test_bst.insert(3)
    test_bst.insert(5)
    test_bst.insert(4)
    test_bst.insert(9)
    test_bst.insert(1)
    test_bst.insert(15)
    test_bst.insert(2)
    test_bst.insert(8)
    test_bst.insert(12)
    return test_bst


def test_node_is_node_class():
    """Test that node is an instance of Node."""
    from bst import Node
    n = Node(1)
    assert isinstance(n, Node)


def test_bst_is_bst_object():
    """Test that bst is an instance of BST."""
    from bst import BinarySearchTree
    tree = BinarySearchTree()
    assert isinstance(tree, BinarySearchTree)


def test_insert_one_node_on_empty_tree(empty_tree):
    """Test that inserted node on empty tree sets root to node."""
    empty_tree.insert(6)
    assert empty_tree._root.val == 6


def test_insert_node_with_string_as_value(empty_tree):
    """Test for TypeError when value is a string."""
    with pytest.raises(TypeError):
        empty_tree.insert('potato')


def test_insert_method_inserts_nodes(empty_tree):
    """Test that insert method inserts nodes in correct order."""
    empty_tree.insert(1)
    empty_tree.insert(5)
    empty_tree.insert(7)
    empty_tree.insert(6)
    assert empty_tree._root.right.right.left.val == 6


def test_size_empty_tree(empty_tree):
    """Test size attr is 0 with empty tree."""
    assert empty_tree.size() == 0


def test_size_full_tree(full_tree):
    """Test size attr is correct size of tree with nodes."""
    assert full_tree.size() == 10


def test_depth_empty_tree(empty_tree):
    """Test depth attr is 0 with empty tree."""
    assert empty_tree.depth() == 0


def test_depth_full_tree(full_tree):
    """Test depth attr is correct depth of tree with nodes."""
    assert full_tree.depth() == 3


def test_balance_on_empty_tree(empty_tree):
    """"Test balance method returns 0 on empty tree."""
    assert empty_tree.balance() == 0


def test_node_has_correct_children(full_tree):
    """Test that a node has the correct children."""
    node = full_tree.search(3)
    assert node.left.val == 1 and node.right.val == 5


def test_search_returns_none_on_empty_tree(empty_tree):
    """Test that search method returns None on empty tree."""
    assert empty_tree.search(13) is None


def test_search_returns_none_on_non_existent_node(full_tree):
    """Test that search method returns None with non-existent node."""
    assert full_tree.search(33) is None


def test_search_returns_node_obj_when_found(full_tree):
    """Test that search method returns Node object when node is found."""
    from bst import Node
    assert isinstance(full_tree.search(3), Node)


def test_search_returns_node_with_correct_value_when_found(full_tree):
    """Test that search method returns Node with correct value when found."""
    assert full_tree.search(3).val == 3


def test_contains_returns_false_on_empty_tree(empty_tree):
    """Test that contains method returns False on empty tree."""
    assert empty_tree.contains(3) is False


def test_contains_returns_false_on_non_existent_node(full_tree):
    """Test that contains method returns False with non-existent node."""
    assert full_tree.contains(33) is False


def test_contains_returns_true_with_root_node(full_tree):
    """Test that contains method returns True with root node."""
    assert full_tree.contains(3) is True


def test_breadth_first_method_returns_a_generator(full_tree):
    """Test the breadth_first method returns a generator."""
    breadth_first_gen = full_tree.breadth_first()
    assert isinstance(breadth_first_gen, types.GeneratorType)


def test_breadth_first_method_returns_empty_gen_with_empty_tree(empty_tree):
    """Test the breadth_first method returns a empty gen with empty tree."""
    breadth_first_gen = empty_tree.breadth_first()
    assert [n for n in breadth_first_gen] == []


def test_breadth_first_method_correctly_traverses_bst(full_tree):
    """Test the breadth_first method works correctly."""
    breadth_first_gen = full_tree.breadth_first()
    assert [n for n in breadth_first_gen] == [6, 3, 9, 1, 5, 8, 15, 2, 4, 12]


def test_in_order_method_returns_a_generator(full_tree):
    """Test the in-order method returns a generator."""
    in_order_gen = full_tree.in_order()
    assert isinstance(in_order_gen, types.GeneratorType)


def test_in_order_method_returns_empty_gen_with_empty_tree(empty_tree):
    """Test the in-order method returns a empty gen with empty tree."""
    in_order_gen = empty_tree.in_order()
    assert [n for n in in_order_gen] == []


def test_in_order_method_correctly_traverses_bst(full_tree):
    """Test the in-order method works correctly."""
    in_order_gen = full_tree.in_order()
    assert [n for n in in_order_gen] == [1, 2, 3, 4, 5, 6, 8, 9, 12, 15]


def test_pre_order_method_returns_a_generator(full_tree):
    """Test the pre-order method returns a generator."""
    pre_order_gen = full_tree.pre_order()
    assert isinstance(pre_order_gen, types.GeneratorType)


def test_pre_order_method_returns_empty_gen_with_empty_tree(empty_tree):
    """Test the pre-order method returns a empty gen with empty tree."""
    pre_order_gen = empty_tree.pre_order()
    assert [n for n in pre_order_gen] == []


def test_pre_order_method_correctly_traverses_bst(full_tree):
    """Test the pre-order method works correctly."""
    pre_order_gen = full_tree.pre_order()
    assert [n for n in pre_order_gen] == [6, 3, 1, 2, 5, 4, 9, 8, 15, 12]


def test_post_order_method_returns_a_generator(full_tree):
    """Test the post-order method returns a generator."""
    post_order_gen = full_tree.post_order()
    assert isinstance(post_order_gen, types.GeneratorType)


def test_post_order_method_returns_empty_gen_with_empty_tree(empty_tree):
    """Test the post-order method returns a empty gen with empty tree."""
    post_order_gen = empty_tree.post_order()
    assert [n for n in post_order_gen] == []


def test_post_order_method_correctly_traverses_bst(full_tree):
    """Test the post-order method works correctly."""
    post_order_gen = full_tree.post_order()
    assert [n for n in post_order_gen] == [2, 1, 4, 5, 3, 8, 12, 15, 9, 6]


def test_delete_works_on_leaf_node(full_tree):
    """Test the delete method deletes a leaf node."""
    full_tree.delete(2)
    in_order_gen = full_tree.in_order()
    assert [n for n in in_order_gen] == [1, 3, 4, 5, 6, 8, 9, 12, 15]


def test_delete_works_on_node_with_one_child(full_tree):
    """Test the delete method deletes a node with one child."""
    full_tree.delete(1)
    in_order_gen = full_tree.in_order()
    assert [n for n in in_order_gen] == [2, 3, 4, 5, 6, 8, 9, 12, 15]


def test_delete_works_on_non_root_node_with_two_children(full_tree):
    """Test the delete method deletes non-root node with two kids."""
    full_tree.delete(3)
    in_order_gen = full_tree.in_order()
    assert [n for n in in_order_gen] == [1, 2, 4, 5, 6, 8, 9, 12, 15]


def test_delete_works_on_root(full_tree):
    """Test the delete method deletes the root."""
    full_tree.delete(6)
    in_order_gen = full_tree.in_order()
    assert [n for n in in_order_gen] == [1, 2, 3, 4, 5, 8, 9, 12, 15]


def test_delete_all_nodes(full_tree):
    """Test the delete method deletes all the nodes."""
    for i in [1, 2, 3, 4, 5, 6, 8, 9, 12, 15]:
        full_tree.delete(i)
    in_order_gen = full_tree.in_order()
    assert [n for n in in_order_gen] == []


def test_delete_empty_tree(empty_tree):
    """Test the delete method on an empty tree."""
    empty_tree.delete(3)
    in_order_gen = empty_tree.in_order()
    assert [n for n in in_order_gen] == []
