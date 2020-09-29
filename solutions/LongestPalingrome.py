import random

# Question: Given a string, find the longest palindrome substring
# ex1: given "ABABABA" should return 7
#   because the longest palingrome substring is "ABABABA"
# ex2" given "BBBABA"
#    return 3
# reference solution: https://blog.crimx.com/2017/07/06/manachers-algorithm/

class Solution(object):
    def longestPalindromeSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        preprocess_s = ''
        for ch in s:
            preprocess_s += ch + '#'
        preprocess_s = '$#' + preprocess_s + '@'

        # start solution
        C = 0
        R = 0
        dp = [0] * len(preprocess_s)
        for i in range(1, len(preprocess_s)-1):
            mirr = 2 * C - i
            if i < R:
                dp[i] = min(dp[mirr], R - i)

            while (preprocess_s[i + (dp[i] + 1)] == preprocess_s[i - (dp[i] + 1)]):
                dp[i] += 1
            if i + dp[i] > R:
                R = i + dp[i]
                C = i

        return max(dp)
