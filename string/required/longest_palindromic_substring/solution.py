class Solution:
    """https://www.lintcode.com/problem/200/?_from=collection&fromId=161
    Description
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

Example
Example 1:

Input:"abcdzdcab"
Output:"cdzdc"
Example 2:

Input:"aba"
Output:"aba"
Challenge
O(n2) time is acceptable. Can you do it in O(n) time.

Tags
Company
Amazon
Microsoft
Bloomberg
Uber
Related Problems
916
Palindrome Permutation
Easy
893
Longest Palindromic Substring II
Hard
775
Palindrome Pairs
Hard
667
Longest Palindromic Subsequence
Medium
415
Valid Palindrome
Medium
200
Longest Palindromic Substring
Medium
108
Palindrome Partitioning II
Medium

    @param s: input string
    @return: a string as the longest palindromic substring
    """
    def longestPalindrome(self, s):
        if not s:
            return ""
        n = len(s)
        # deep copy, avoid copied arr points to the same arr
        is_palindrome = [[False] * n for _ in range(n)]
        for i in range(n):
            is_palindrome[i][i] = True
        # empty string / invalid string
        for i in range(1, n):
            is_palindrome[i][i - 1] = True
        start, longest = 0, 1
        # 填表顺序遍历 从小到大 长度
        for length in range(2, n + 1):
            for i in range(n - length + 1): # 遍历起始位置
                j = i + length - 1
                is_palindrome[i][j] = is_palindrome[i + 1][j - 1] and s[i] == s[j]
                if is_palindrome[i][j] and length > longest:
                    start, longest = i, length
        return s[start:start + longest]