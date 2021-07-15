class Solution:
    """https://www.lintcode.com/problem/192/?_from=collection&fromId=161
    HARD
    Description
Implement wildcard pattern matching with support for '?' and '*'.The matching rules are as follows：

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

0 <= |s|, |p| <= 1000
It is guaranteed that 𝑠 only contains lowercase Latin letters and p contains lowercase Latin letters , ? and *

Example
Example 1

Input:
"aa"
"a"
Output: false
Example 2

Input:
"aa"
"aa"
Output: true
Example 3

Input:
"aaa"
"aa"
Output: false
Example 4

Input:
"aa"
"*"
Output: true
Explanation: '*' can replace any string
Example 5

Input:
"aa"
"a*"
Output: true
Example 6

Input:
"ab"
"?*"
Output: true
Explanation: '?' -> 'a' '*' -> 'b'
Example 7

Input:
"aab"
"c*a*b"
Output: false
Tags
Dynamic Programming/DP
Two Sequences DP
Memoization Search
Related Problems
154
Regular Expression Matching
Hard

    @param source: A string
    @param pattern: A string includes "?" and "*"
    @return: is Match?
    """

    def isMatch(self, source, pattern):
        if source is None or pattern is None:
            return False
        return self.is_match_helper(source, 0, pattern, 0, {})

    def all_star(self, pattern, p_index):  # check if pattern[j:len(pattern)] are all *
        for i in range(p_index, len(pattern)):
            if pattern[i] != '*':
                return False
        return True

    def is_match_char(self, s, p):
        return s == p or p == '?'

    def is_match_helper(self, source, i, pattern, j, memo):
        if (i, j) in memo:  # check memo
            return memo[(i, j)]
        # len(pattern) > len(source) s is used up, every char after this point in pattern should be star
        if i == len(source):
            return self.all_star(pattern, j)
        if j == len(pattern):  # pattern string already used up
            return i == len(source)
        if pattern[j] != '*':
            matched = self.is_match_char(source[i], pattern[j]) and self.is_match_helper(source, i + 1,
                                                                                         pattern, j + 1, memo)
        else:  # pattern char == *, * match s[i] advance s ptr || or * match none + advanced p ptr
            matched = self.is_match_helper(source, i + 1, pattern, j, memo) \
                      or self.is_match_helper(source, i, pattern, j + 1, memo)
        memo[(i, j)] = matched  # keep res in memo
        return matched
