# directional offsets
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]


class Solution:
    """https://www.lintcode.com/problem/132/?_from=collection&fromId=161
    Description
Given a matrix of lower alphabets and a dictionary. Find all words in the dictionary that can be found in the matrix. A word can start from any position in the matrix and go left/right/up/down to the adjacent position. One character only be used once in one word. No same word in dictionary

Example
Example 1:

Input：["doaf","agai","dcan"]，["dog","dad","dgdg","can","again"]
Output：["again","can","dad","dog"]
Explanation：
  d o a f
  a g a i
  d c a n
search in Matrix，so return ["again","can","dad","dog"].
Example 2:

Input：["a"]，["b"]
Output：[]
Explanation：
 a
search in Matrix，return [].
Challenge
Using trie to implement your algorithm
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """

    def wordSearchII(self, board, words):
        if not board:
            return []
        word_set = set(words)
        prefix_set = set()
        for word in words:
            for i in range(len(word)):
                prefix_set.add(word[:i + 1])
        result_set = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.search(board, i, j, board[i][j], word_set, prefix_set,
                            {(i, j)}, result_set)
        return list(result_set)

    def search(self, board, x, y, word, word_set, prefix_set, visited, result_set):
        # word: the word found in current dfs path, visited: visited point in current path
        if word not in prefix_set:
            return
        # if found a word, record it and continue because there maybe other word with same prefix
        if word in word_set:
            result_set.add(word)
        for dx, dy in DIRECTIONS:
            x_ = x + dx
            y_ = y + dy
            # pruning for invalid points or visited points
            if not self.inside(board, x_, y_) or (x_, y_) in visited:
                continue
            visited.add((x_, y_))
            # recurse on remaining problem by dfs
            self.search(board, x_, y_, word + board[x_][y_],
                        word_set, prefix_set, visited, result_set)
            visited.remove((x_, y_))  # backtracking last move to try on new move

    # check if a point is inside board
    def inside(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])
