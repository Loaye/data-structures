"""Fixtures for tests"""

@pytest.fixture
def priq():
    """Create empty priq."""
    from priorityq import PriorityQueue
    new_priq = PriorityQueue()
    return new_priq