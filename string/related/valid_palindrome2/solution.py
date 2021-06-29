# follow up 可以删除最多一个字符, 没有不合法字符 判断是不是palindrome   巧用子函数避免重复代码
# https://www.lintcode.com/problem/valid-palindrome-ii/
class Solution:
    """
    Description
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

The string will only contain lowercase characters.
The maximum length of the string is 50000.
Example
Example 1:

Input: s = "aba"
Output: true
Explanation: Originally a palindrome.
Example 2:

Input: s = "abca"
Output: true
Explanation: Delete 'b' or 'c'.
Example 3:

Input: s = "abc"
Output: false
Explanation: Deleting any letter can not make it a palindrome.
Tags
Opposite Direction Two Pointers
Greedy
Two Pointers
Company
Facebook
NetEase
    @param s: a string
    @return: whether you can make s a palindrome by deleting at most one character
    """

    def find_first_different_pair(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return left, right
            left += 1
            right -= 1
        return left, right

    def validPalindrome(self, s):
        if not s:
            return False
        s_is_palindrome, left, right = self.is_palindrome(s, 0, len(s) - 1)
        if s_is_palindrome:
            return True
        return self.is_palindrome(s, left + 1, right)[0] or self.is_palindrome(s, left, right - 1)[0]

    def is_palindrome(self, s, left, right):
        left, right = self.find_first_different_pair(s, left, right)
        return left >= right, left, right

