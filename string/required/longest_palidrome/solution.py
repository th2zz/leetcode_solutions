class Solution:
    """https://www.lintcode.com/problem/627/?_from=collection&fromId=161
    Description
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Assume the length of given string will not exceed 100000.

Example
Example 1:

Input : s = "abccccdd"
Output : 7
Explanation :
One longest palindrome that can be built is "dccaccd", whose length is `7`.
Tags
Hash Table
Company
Google
Amazon
Related Problems
916
Palindrome Permutation
Easy
891
Valid Palindrome II
Medium
745
Palindromic Ranges
Medium
678
Shortest Palindrome
Medium
415
Valid Palindrome
Medium

    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # aebbbccccdd  create a frequency table
        # a: 1
        # e: 1
        # b: 3
        # c: 4
        # d: 2
        # 取最大的奇数频数 + 所有偶数频数相加 + 其他奇数频数均少取一个
        if not s:
            return 0
        frequency_table = {}
        # O(n) get frequency table
        for char in s:
            if char not in frequency_table:
                frequency_table[char] = 1
            else:
                frequency_table[char] += 1
        sum, odd_num_cnt = 0, 0
        for char, frequency in frequency_table.items():
            sum += frequency
            if frequency % 2 == 1:
                odd_num_cnt += 1
        if odd_num_cnt >= 1:
            return sum - (odd_num_cnt - 1)
        else:
            return sum

# print(Solution().longestPalindrome("bb"))

