"""Tests for queue data structure."""


def test_queue_init():
    """Test if queue is created."""
    from queue import Queue
    queue = Queue()
    assert queuetest._length == 0


def test_queue_enqueue_two_nodes():
    """Test if able to enqueue two nodes."""
    from queue import Queue
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(10)
    assert queue._dll.tail.data == queue.length(2)


def test_dequeue_node():
    """Test is node was dequeued."""
    from queue import Queue
    queue = Queue()
    queue.enqueue(15)
    queue.enqueue(10)
    assert queue.dequeue() == 15


def test_dequeue_node_length():
    """Test if able to dequeue a node."""
    from queue import Queue
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(10)
    queue.dequeue()
    assert queue.length == 1


def test_dequeue_head_is_tail_with_one_node():
    """Test if head and tail are the same."""
    from queue import Queue
    queue = Queue()
    queue.enqueue(25)
    queue.enqueue(20)
    queue.dequeue()
    assert queue._dll.tail == queue._dll.head


def test_peek():
    """Test if next value to be removed."""
    from queue import Queue
    queue = Queue()
    queue.enqueue(105)
    queue.enqueue(5)
    assert queue.peek() == 105


def test_queue_is_empty_peek():
    """Test calling peek on empty returns None."""
    from queue import Queue
    queue = Queue()
    assert queue.peek() is None
