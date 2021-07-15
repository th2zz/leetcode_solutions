class Solution:
    """https://www.lintcode.com/problem/154/?_from=collection&fromId=161
    Algorithms
Hard
Accepted Rate
31%

The implementation supports regular expression matching for '.' and '*'.
'.' matches any single character.
'*' matches zero or more of the preceding elements, before '*' is guaranteed to be a non-'*' element.
The match should cover the entire input string, not just a part of it.
The function that needs to be implemented is:
bool isMatch(string s, string p)

isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
Example
Example 1:

Input: "aa", "a"
Output: false
Explanation:
Can't match
Example 2:

Input: "aa", "a*"
Output: true
Explanation:
'*' can repeat a
Example 3:

Input: "aab", "c*a*b"
Output: true
Explanation:
"c*" matches 0'c' as a whole, which is ""
"a*" matches 2'a' as a whole, which is "aa"
"b" matches "b"
So "c*a*b" can match "aab"
``` repeat a

Tags
Dynamic Programming/DP
Two Sequences DP
Memoization Search
Related Problems
192
Wildcard Matching
Hard

    @param source: A string
    @param pattern: A string includes "." and "*"
    @return: A boolean
    """

    def isMatch(self, source, pattern):
        if source is None or pattern is None:
            return False
        return self.is_match_helper(source, 0, pattern, 0, {})

    def is_match_helper(self, source, i, pattern, j, memo):
        if len(pattern) == j:
            return len(source) == i
        if len(source) == i:
            return self.is_empty(pattern[j:])
        if (i, j) in memo:
            return memo[(i, j)]
        if j + 1 < len(pattern) and pattern[j + 1] == '*':# * not match char || * repeat previous char to match s
            matched = self.is_match_helper(source, i, pattern, j + 2, memo) \
                      or self.is_match_char(source[i], pattern[j]) and \
                      self.is_match_helper(source, i + 1, pattern, j, memo)
        else:
            matched = self.is_match_char(source[i], pattern[j]) and self.is_match_helper(source, i + 1,
                                                                                         pattern, j + 1, memo)
        memo[(i, j)] = matched
        return matched

    def is_match_char(self, s, p):
        return s == p or p == '.'

    def is_empty(self, pattern):
        # '*' matches zero or more of the preceding elements, before '*' is guaranteed to be a non-'*' element.
        # traverse remaining pattern with strip 2, if char not * or not exist(out of bound) return False
        for i in range(0, len(pattern), 2):  # has to be even length
            if i + 1 >= len(pattern) or pattern[i + 1] != '*':
                return False
        return True
# print(Solution().isMatch('aa', '.*'))
