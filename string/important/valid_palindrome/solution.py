# https://www.lintcode.com/problem/valid-palindrome/
# 判断是不是回文串 非法字符需跳过
class Solution:
    """
    Description
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

Example
Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama"
Example 2:

Input: "race a car"
Output: false
Explanation: "raceacar"
Challenge
O(n) time without extra memory.

Tags
Two Pointers
Company
LinkedIn
Facebook
Zenefits
Microsoft
Uber
Related Problems
893
Longest Palindromic Substring II
Hard
891
Valid Palindrome II
Medium
745
Palindromic Ranges
Medium
744
Sum of first K even-length Palindrome numbers
Medium
491
Palindrome Number
Easy
627
Longest Palindrome
Easy
223
Palindrome Linked List
Medium
200
Longest Palindromic Substring
Medium
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def is_char_valid(self, char):
        return char.isdigit() or char.isalpha()
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not self.is_char_valid(s[left]):
                left += 1
            while left < right and not self.is_char_valid(s[right]):
                right -= 1
            if left < right and s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
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
        # left, right 左边右边届index
        s_is_palindrome, left, right = self.is_palindrome(s, 0, len(s) - 1)
        if s_is_palindrome:
            return True
        # 查看左边去掉一个字符 和 右边去掉一个字符的子串是不是palindrome
        return self.is_palindrome(s, left + 1, right)[0] or self.is_palindrome(s, left, right - 1)[0]

    def is_palindrome(self, s, left, right):
        left, right = self.find_first_different_pair(s, left, right)
        return left >= right, left, right