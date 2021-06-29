

KEYBOARD = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
class Solution:
    """https://www.lintcode.com/problem/425/?_from=collection&fromId=161
    Description
Given a digit string excluded 0 and 1, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

1	2
ABC	3
DEF
4
GHI	5
JKL	6
MNO
7
PQRS	8
TUV	9
WXYZ
Although the answer above is in lexicographical order, your answer could be in any order you want.

Example
Example 1:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
Explanation:
'2' could be 'a', 'b' or 'c'
'3' could be 'd', 'e' or 'f'
Example 2:

Input: "5"
Output: ["j", "k", "l"]

    @param digits: A digital string
    @return: all posible letter combinations
    """

    def letterCombinations(self, digits):
        combinations = []
        if not digits:
            return combinations
        self.dfs(digits, 0, "", combinations)
        return combinations

    def dfs(self, digits, index, combination, combinations):
        """dfs on given digital string "digits" e.g. 23456 to search for all possible letter combination

        Args:
            digits (str): digital string  e.g. 23456
            index (int): current position in digital string digits
            combination (str): current combination, can be backtracked during recursion
            combinations (list): current solution set

        Returns:

        """
        if index == len(digits):
            combinations.append(combination)
            return
        digit = int(digits[index])
        for i in range(len(KEYBOARD[digit])):  # traverse all possible char for each number
            self.dfs(digits, index + 1, combination + KEYBOARD[digit][i], combinations)
            # no backtrack because of call by value, combination will not be changed

