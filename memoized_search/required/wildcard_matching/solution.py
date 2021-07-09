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

    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        if s is None or p is None:
            return False
        return self.is_match_helper(s, 0, p, 0, {})

    def all_star(self, pattern, p_index):  # check if pattern[p_index:len(pattern)] are all *
        for i in range(p_index, len(pattern)):
            if pattern[i] != '*':
                return False
        return True

    def is_match_char(self, s_char, p_char):
        return s_char == p_char or p_char == '?'

    def is_match_helper(self, source, s_index, pattern, p_index, memo):
        if p_index == len(pattern):  # pattern string already used up
            return s_index == len(source)
        if s_index == len(source):  # pattern比s长 s用完了 p后面必须全是star
            return self.all_star(pattern, p_index)
        if (s_index, p_index) in memo:  # check memo
            return memo[(s_index, p_index)]
        s_char = source[s_index]
        p_char = pattern[p_index]
        match = False
        if p_char != '*':
            match = self.is_match_char(s_char, p_char) and self.is_match_helper(source, s_index + 1,
                                                                                pattern, p_index + 1, memo)
        else:  # pattern char == *, * match s[s_index] advance s ptr || or * match none + advanced p ptr
            match = self.is_match_helper(source, s_index + 1, pattern, p_index, memo) \
                    or self.is_match_helper(source, s_index, pattern, p_index + 1, memo)
        memo[(s_index, p_index)] = match  # keep res in memo
        return match
