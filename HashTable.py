"""
    Hash Tables:
        - are used to store and retrieve key-value pairs effectively.
        - offer fast lookup, insertion and deletion.
        - Best case: O(1),  Worst case: O(n)
        - Used in various applications, including databases, caches, and language implementations.

        Hash Function:
            - map keys to indices in an array called the hash table/map.
            - takes a key as input and produces fixed-sized hash code (integer within range of array indices).
            - distributes keys uniformly across the array to minimize collisions (two keys mapping to the same index).

        Array (Hash Table):
            - the hash table is an array of fixed or dynamic size, where each slot or bucket corresponds to an index
                generated by the hash function.
            - Each slot may contain a linked list, array, or some other data structure.

        Collision Handling:
            - occurs when 2 different keys hash to the same index.
            - Open Addressing: When a collision occurs, search for the next available slot.
"""


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash(key)
        self.table[index].append((key, value))

    def delete(self, key):
        index = self.hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return

    def lookup(self, key):
        index = self.hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v

        return None


ht = HashTable(10)
ht.insert("apple", 5)
ht.insert("banana", 7)
print(ht.lookup("apple"))
ht.delete("apple")
print(ht.lookup("apple"))
