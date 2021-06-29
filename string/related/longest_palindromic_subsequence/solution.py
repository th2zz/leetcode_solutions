class Solution:
    """
    Description
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example
Example1

Input: "bbbab"
Output: 4
Explanation:
One possible longest palindromic subsequence is "bbbb".
Example2

Input: "bbbbb"
Output: 5
Tags
Company
Uber
Amazon
Related Problems
775
Palindrome Pairs
Hard
738
Count Different Palindromic Subsequences
Hard
678
Shortest Palindrome
Medium
200
Longest Palindromic Substring
Medium

    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    bbbab res bbbb 4
    bbbbb res bbbbb 5
    brute force O(n * 2^n)
    https://leetcode-cn.com/problems/longest-palindromic-subsequence/solution/zi-xu-lie-wen-ti-tong-yong-si-lu-zui-chang-hui-wen/
    """
    def longestPalindromeSubseq(self, s):
        if not s:
            return 0
        n = len(s)
        length = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            length[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    length[i][j] = length[i + 1][j - 1] + 2
                else:
                    length[i][j] = max(length[i + 1][j], length[i][j - 1])
        return length[0][n - 1]