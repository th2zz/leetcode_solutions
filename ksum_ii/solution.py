class Solution:
    """https://www.lintcode.com/problem/90/?_from=collection&fromId=161
    Description
Given n unique postive integers, number k (1<=k<=n1<=k<=n) and target.

Find all possible k integers where their sum is target.

Example
Example 1:

Input:

array = [1,2,3,4]
k = 2
target = 5
Output:

[[1,4],[2,3]]
Explanation:

1+4=5,2+3=5

Example 2:

Input:

array = [1,3,4,6]
k = 3
target = 8
Output:

[[1,3,4]]
Explanation:

1+3+4=8
    @param A: an integer array
    @param k: a postive integer <= length(A)
    @param targer: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        A = sorted(A)  # no need to sort because we are not following lexicographical order and no duplication here
        subsets = []
        self.dfs(A, 0, k, target, [], subsets)
        return subsets

    def dfs(self, A, index, k, target, subset, subsets):
        # starting from A[index]: choose k numbers and put in subset, such that k sum = target
        if k == 0 and target == 0:  # found 1 solution
            subsets.append(list(subset))
            return
        if k == 0 or target <= 0:  # pruning for invalid recursion parameters
            return
        for i in range(index, len(A)):  # decomposition and advancement of recursion
            subset.append(A[i])  # include A[i] and dfs recurse on remaining problem
            self.dfs(A, i + 1, k - 1, target - A[i], subset, subsets)
            subset.pop()  # backtracking try on A[i]
