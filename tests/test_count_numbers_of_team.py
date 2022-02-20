import pytest

from solutions.countNumbersOfTeam import Solution

def test_heap_sort():
    assert Solution().numTeams([2,5,3,4,1]) == 3
    assert Solution().numTeams([2,1,3]) == 0

