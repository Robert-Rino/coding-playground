import pytest

from solutions.lru import LRU

def test_lru():
    lru = LRU(3)
    assert lru.get('a') == None

    lru.put('a', 1)
    lru.put('b', 2)
    assert lru.get('a') == 1

    lru.put('c', 3)
    lru.put('d', 4)
    assert lru.get('b') == None
