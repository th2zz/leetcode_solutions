class Solution:
    """https://www.lintcode.com/problem/683/?_from=collection&fromId=161
    Description
Give a dictionary of words and a sentence with all whitespace removed, return the number of sentences you can form by
inserting whitespaces to the sentence so that each word can be found in the dictionary.

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
    @return: the number of possible sentences. / how many ways to form the sentence with given words in dict
    can we use a word multiple times: no
    """
    def wordBreak3(self, s, dict):
        if not s or not dict:
            return 0
        max_len, lower_dict = self.initialize(dict)
        # word break by dfs
        return self.memo_search(s.lower(), 0, max_len, lower_dict, {})

    def initialize(self, dict):
        max_len, lower_dict = 0, set()  # 把所有词转成小写 记录最长word长度
        for word in dict:
            max_len = max(max_len, len(word))
            lower_dict.add(word.lower())
        return max_len, lower_dict

    def memo_search(self, s, index, max_len, lower_dict, memo):
        if index == len(s):
            return 1
        if index in memo:  # s[index..] processed before, return result
            return memo[index]
        result = 0  # s[index..] 方案总数
        for end in range(index + 1, len(s) + 1):  # enumerate word end exclusive end range [index + 1, len(s)]
            if end - index > max_len:  # pruning based on max len in all words
                break  # end - index = [index, ..., end - 1] [index...]substring length
            word = s[index: end]  # get s substring [index, ..., end - 1] as word
            if word not in lower_dict:  # skip if it is not in dict
                continue  # recurse on s[end..] add that to current result
            result += self.memo_search(s, end, max_len, lower_dict, memo)  # 这个word end就是下个word开始 find sol at index end
        memo[index] = result  # memo: # possible sentences formed from s[index..]
        return memo[index]  # original problem solution: memo[0]
