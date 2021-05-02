# follow up 可以删除最多一个字符, 没有不合法字符 判断是不是palindrome   巧用子函数避免重复代码
# https://www.lintcode.com/problem/valid-palindrome-ii/
class Solution:
    """
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

