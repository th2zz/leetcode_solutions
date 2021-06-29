from collections import deque
class Solution:
    """https://www.lintcode.com/problem/120/?_from=collection&fromId=161
    Description
Given two words (start and end), and a dictionary, find the shortest transformation sequence from start to end, output the length of the sequence.
Transformation rule such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary. (Start and end words do not need to appear in the dictionary )
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the dictionary.
You may assume beginWord and endWord are non-empty and are not the same.
len(dict) <= 5000, len(start) < 5len(dict)<=5000,len(start)<5
Example
Example 1:

Input:

start = "a"
end = "c"
dict =["a","b","c"]
Output:

2
Explanation:

"a"->"c"

Example 2:

Input:

start ="hit"
end = "cog"
dict =["hot","dot","dog","lot","log"]
Output:

5
Explanation:

"hit"->"hot"->"dot"->"dog"->"cog"


    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, d):
        # assume dict not none
        # assume beginWord and endWord non empty and not equal
        # must add end, can add start
        d.add(end)
        queue = collections.deque([start])
        visited = set([start])
        distance = 0
        while queue:
            # length to current level
            distance += 1
            size = len(queue)
            for i in range(size):
                word = queue.popleft()
                # if reach target word return result
                if word == end:
                    return distance
                # get next word
                for next_word in self.get_next_words(word, d):
                    if next_word in visited:
                        continue
                    queue.append(next_word)
                    visited.add(next_word)
        return 0

    # find all words that can be laddered after the word
    # e.g. word = 'hot' d = {'hot', 'hit', 'hog'}, return {'hit', 'hog'}
    def get_next_words(self, word, d):
        next_words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                # switch character at index i to char in new word
                new_word = left + char + right
                if new_word in d:
                    next_words.append(new_word)
        return next_words
