import pytest

from solutions.LongestPalingrome import Solution

def test_longest_palingrome():
    assert Solution().longestPalindromeSubstring('ABABA') == 5
