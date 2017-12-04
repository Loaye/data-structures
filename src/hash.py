"""My attempt at a hash table."""


class Item:
    """Set Item class."""

    key = ""
    value = 0

    def __init__(self, key, value):
        """Initialize table."""
        self.key = key
        self.value = value

    def print(self):
        """."""
        print("  '" + self.key + "' / " + str(self.value))


class HashTable:
    """Common base class for a hash table."""

    tableSize = 0
    entriesCount = 0
    alphabetSize = 2 * 26
    hashTable = []

    def __init__(self, size):
        """."""
        self.tableSize = size
        self.hashTable = [[] for i in range(size)]

    def char2int(self, char):
        """Turn alpha into Int."""
        if char >= 'A' and char <= 'Z':
            return ord(char) - 65
        elif char >= 'a' and char <= 'z':
            return ord(char) - 65 - 7
        else:
            raise NameError('Invalid character in key! Alphabet is [a-z][A-Z]')

    def hashing(self, key):
        """Set up hash to find proper spot."""
        hash = 0
        for i, c in enumerate(key):
            hash += pow(self.alphabetSize, len(key) - i - 1) * self.char2int(c)
        return hash % self.tableSize

    def insert(self, item):
        """Insert a value into the table."""
        hash = self.hashing(item.key)
        # print(hash)
        for i, it in enumerate(self.hashTable[hash]):
            if it.key == item.key:
                del self.hashTable[hash][i]
                self.entriesCount -= 1
        self.hashTable[hash].append(item)
        self.entriesCount += 1

    def get(self, key):
        """Find a value and return it."""
        print("Getting item(s) with key '" + key + "'")
        hash = self.hashing(key)
        for i, it in enumerate(self.hashTable[hash]):
            if it.key == key:
                return self.hashTable[hash]
        print(" NOT IN TABLE!")
        return None

    def delete(self, key):
        """Delete a valur frmo the table."""
        print("Deleting item with key '" + key + "'")
        hash = self.hashing(key)
        for i, it in enumerate(self.hashTable[hash]):
            if it.key == key:
                del self.hashTable[hash][i]
                self.entriesCount -= 1
                return
        print(" NOT IN TABLE!")

    def print(self):
        """Print the value in the table."""
        print(">>>>> CURRENT TABLE BEGIN >>>>")
        print(str(self.getNumEntries()) + " entries in table")
        for i in range(self.tableSize):
            print(" [" + str(i) + "]: ")
            for j in range(len(self.hashTable[i])):
                self.hashTable[i][j].print()
        print("<<<<< CURRENT TABLE END <<<<<")

    def getNumEntries(self):
        """Return the count of the values in the table."""
        return self.entriesCount

if __name__ == "__main__":
    hs = HashTable(11)

    item = Item("one", 1)
    hs.insert(item)
    hs.print()
    hs.insert(item)
    hs.print()

    item = Item("two", 2)
    hs.insert(item)

    item = Item("three", 3)
    hs.insert(item)
    hs.print()

    item = Item("one", 4)
    hs.insert(item)

    items = hs.get("one")
    if items is not None:
        for j in range(len(items)):
            items[j].print()

    item = Item("PheewThisIsALongOne", 12345)
    hs.insert(item)
    hs.print()

    items = hs.get("PheewThisIsALongOne")
    if items is not None:
        for j in range(len(items)):
            items[j].print()

    items = hs.get("PheewThisIsOne")
    if items is not None:
        for j in range(len(items)):
            items[j].print()

    hs.delete("PheewThisIsALongOne")
    hs.print()

    hs.delete("PheewThisIsTheOne")
    hs.print()

    hs.delete("one")
    hs.print()

    # This one leads to an exception as '!' is not part of the allowed alphabet
    # item = Item("!", 5)
    # hs.insert(item)
