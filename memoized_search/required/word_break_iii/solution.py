class Solution:
    """https://www.lintcode.com/problem/683/?_from=collection&fromId=161
    Description
Give a dictionary of words and a sentence with all whitespace removed, return the number of sentences you can form by inserting whitespaces to the sentence so that each word can be found in the dictionary.

Ignore case

Example
Example1

Input:
"CatMat"
["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"]
Output: 3
Explanation:
we can form 3 sentences, as follows:
"CatMat" = "Cat" + "Mat"
"CatMat" = "Ca" + "tM" + "at"
"CatMat" = "C" + "at" + "Mat"
Example1

Input:
"a"
[]
Output:
0

Tags
Dynamic Programming/DP
Partition DP


    @param s: A string
    @param dict: A set of word
    @return: the number of possible sentences.
    """
    def wordBreak3(self, s, dict):
        if not s or not dict:
            return 0
        max_len, lower_dict = self.initialize(dict)
        return self.memo_search(s.lower(), 0, max_len, lower_dict, {})

    def initialize(self, dict):
        max_len, lower_dict = 0, {}  # 把所有词转成小写 记录最长长度
        for word in dict:
            max_len = max(max_len, len(word))
            lower_dict.add(word.lower())
        return max_len, lower_dict

    def memo_search(self, s, index, max_len, lower_dict, memo):
        if index == len(s):
            return 1
        if index in memo:
            return memo[index]
        result = 0
        for end in range(index + 1, len(s) + 1):
            if end - index > max_len:
                break
            word = s[index: end]
            if word not in lower_dict:
                continue
            result += self.memo_search(s, end, max_len, lower_dict, memo)
        memo[index] = result
        return memo[index]
