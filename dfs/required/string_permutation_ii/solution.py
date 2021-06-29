class Solution:
    """https://www.lintcode.com/problem/10/?_from=collection&fromId=161
    Description
Given a string, find all permutations of it without duplicates.

Example
Example 1:

Input:

s = "abb"
Output:

["abb", "bab", "bba"]
Explanation:

There are six kinds of full arrangement of abb, among which there are three kinds after removing duplicates.

Example 2:

Input:

s = "aabb"
Output:

["aabb", "abab", "baba", "bbaa", "abba", "baab"]
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        if not str:
            return [str]
        chars = list(sorted(str))
        visited = [False] * len(chars)
        permutations = []
        self.dfs(chars, visited, [], permutations)
        return permutations

    def dfs(self, chars, visited, permutation, permutations):
        if len(permutation) == len(chars):
            permutations.append(''.join(permutation))
            return
        for i in range(len(chars)):
            if visited[i]:
                continue
            if i > 0 and chars[i - 1] == chars[i] and not visited[i - 1]:
                continue
            visited[i] = True
            permutation.append(chars[i])
            self.dfs(chars, visited, permutation, permutations)
            permutation.pop()
            visited[i] = False
