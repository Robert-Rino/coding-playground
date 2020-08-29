from collections import OrderedDict

class LRU():
    def __init__(self, capacity):
        self.max = capacity
        self._dict = OrderedDict()

    def get(self, key):
        if (value := self._dict.get(key)):
            self.put(key, value)
            return value
        return None

    def put(self, key, value):
        if key in self._dict:
            del self._dict[key]

        self._dict[key] = value

        if len(self._dict) > self.max:
            self._dict.popitem(last=False)

lru = LRU(3)

lru.put(1, 1)
lru.put(2, 2)
lru.put(3, 3)
assert lru.get(1) # 1
lru.put(4, 4)
assert lru.get(2) # None
