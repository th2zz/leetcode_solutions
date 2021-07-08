class Solution:
    """https://www.lintcode.com/problem/582/?_from=collection&fromId=161
    582 · Word Break II
Algorithms
Hard
Accepted Rate
36%

DescriptionSolutionNotesDiscussLeaderboard
Description
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

Example
Example 1:

Input："lintcode"，["de","ding","co","code","lint"]
Output：["lint code", "lint co de"]
Explanation：
insert a space is "lint code"，insert two spaces is "lint co de".
Example 2:

Input："a"，[]
Output：[]
Explanation：dict is null.
Tags
Partition DP
Memoization Search
Depth First Search/DFS
Dynamic Programming/DP
Company
Twitter
Snapchat
Dropbox
Uber
Google
Related Problems
680
Split String
Medium
107
Word Break
Medium

    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences. / how many ways can s be splited s.t. every word is in word dict once
    """

    def wordBreak(self, s, wordDict):
        if not s or not wordDict:
            return []
        max_word_len = len(max(wordDict, key=len))
        return self.dfs(s, max_word_len, wordDict, {})

    def dfs(self, s, max_word_len, wordDict, memo):
        if s in memo:
            return memo[s]
        if len(s) == 0:
            return []
        partitions = []
        for prefix_len in range(1, len(s)):
            if prefix_len > max_word_len:
                break
            prefix = s[:prefix_len]
            if prefix not in wordDict:
                continue
            sub_partitions = self.dfs(s[prefix_len:], max_word_len, wordDict, memo)
            for partition in sub_partitions:
                partitions.append(prefix + " " + partition)  # 当前方案和后面方案拼凑出一个完整方案 如"lint" + "co de"
        if s in wordDict:  # s在input wordDict中 也算一个方案
            partitions.append(s)
        memo[s] = partitions  # book keeping s划分结果
        return partitions
