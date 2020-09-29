import pytest

from solutions.HeapSort import Solution

def test_heap_sort():
    array = [2,1,5,6,4,8,7,9,10,11,13,12,11]
    assert Solution().heap_sort(array) == sorted(array)
