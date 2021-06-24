class Solution:
    """https://www.lintcode.com/problem/135/?_from=collection&fromId=161
    Description
Given a set of candidate numbers candidates and a target number target. Find all unique combinations in candidates
where the numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

All numbers (including target) will be positive integers.
Numbers in a combination a1, a2, … , ak must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak)
Different combinations can be in any order.
The solution set must not contain duplicate combinations.
Example
Example 1:

Input: candidates = [2, 3, 6, 7], target = 7
Output: [[7], [2, 2, 3]]
Example 2:

Input: candidates = [1], target = 3
Output: [[1, 1, 1]]
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        results = []
        if not candidates:
            return results
        # deduplication
        candidates_sorted = sorted(list(set(candidates)))
        self.dfs(candidates_sorted, 0, [], target, results)
        return results

    def dfs(self, candidates, index, current_result, remainingTarget, results):
        if remainingTarget == 0:
            return results.append(list(current_result))
        for i in range(index, len(candidates)):
            if remainingTarget < candidates[i]:
                break
            current_result.append((candidates[i]))
            self.dfs(candidates, i, current_result, remainingTarget - candidates[i], results)
            current_result.pop()
