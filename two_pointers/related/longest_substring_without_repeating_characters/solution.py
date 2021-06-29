class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """https://www.lintcode.com/problem/384/

        Description
Given a string, find the length of the longest substring without repeating characters.

Example
Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The longest substring is "abc".
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The longest substring is "b".
Challenge
time complexity O(n)

Tags
Same Direction Two Pointers
Two Pointers
Company
Adobe
Amazon
Bloomberg
Yelp

Related Problems
928
Longest Substring with At Most Two Distinct Characters
Medium
386
Longest Substring with At Most K Distinct Characters
Medium

        Args:
            s (str): input str

        Returns:
            int: length
brute force do it by looping O(n^2) O(1)

invariant: r指针第一轮后始终位于之前匹配的最长无重复子串的最后一个字符
        """

        n = len(s)
        visited = set()
        res, r = 0, 0
        for l in range(n):
            if l != 0:
                visited.remove(s[l - 1])
            while r in range(n) and s[r] not in visited:
                visited.add(s[r])
                r += 1
            res = max(res, r - l)
        return res
