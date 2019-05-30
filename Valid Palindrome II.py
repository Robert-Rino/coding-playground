'''
Leetcode: https://leetcode.com/problems/valid-palindrome-ii/
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

'''

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1:
            return True

        def is_palin(i, j):
            if i > j:
                return True
            if i == j:
                return True
            if s[i] != s[j]:
                return False
            else:
                return is_palin(i + 1, j - 1)

        for i in range(len(s) / 2):
            if s[i] != s[len(s) - 1 - i]:
                return is_palin(i + 1, len(s) - 1 - i) or is_palin(i, len(s) - 2 - i)
        return True


if __name__ == '__main__':
    s = Solution()
    print s.validPalindrome('ABCA')