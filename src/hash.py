"""Hash Table."""


class Hash(object):
    """Hash class object."""

    def __init__(self, size=10, hash_type='additive'):
        """Initialize Hash."""
        self.table = []
        self._size = size
        for i in range(self._size):
            self.table.append([])

        if hash_type not in ('additive', 'oat'):
            raise ValueError('Invalid hashing function')
        self._hash_type = hash_type

    def _hash(self, key):
        """Hash a passed key."""
        hash = 0
        if self._hash_type == 'additive':
            """Additive Hash Function."""
            for i in key:
                hash += ord(i)
        elif self._hash_type == 'oat':
            """One at a Time Hash Function."""
            for i in key:
                hash += ord(i)
                hash += hash << 10
                hash ^= hash >> 6
            hash += hash << 3
            hash ^= hash >> 11
            hash += hash << 15
        return hash % self._size

    def set(self, key, val):
        """Add a val to the table at index of a hashed key."""
        idx = self._hash(key)
        if len(self.table[idx]) == 0:
            self.table[idx].append([key, val])
        else:
            for i in self.table[idx]:
                if i[0] == key:
                    raise ValueError('Key already in table')
            self.table[idx].append([key, val])
        return

    def get(self, key):
        """Get the val stored at the index of the hashed key."""
        idx = self._hash(key)
        if len(self.table[idx]) == 1:
            return self.table[idx][0][1]
        else:
            for i in self.table[idx]:
                if i[0] == key:
                    return i[1]
            raise KeyError('Key not found')