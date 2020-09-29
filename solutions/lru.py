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
