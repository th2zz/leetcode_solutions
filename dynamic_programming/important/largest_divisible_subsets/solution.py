class Solution:
    """https://www.lintcode.com/problem/603/?_from=collection&fromId=161
    Algorithms
Medium
Accepted Rate
41%

DescriptionSolutionNotesDiscussLeaderboard
Description
Given a set of distinct positive integers, find the largest subset which has the most elements, and every pair of two elements (Si, Sj) in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.
1 \leq len(nums) \leq 500001≤len(nums)≤50000

Example
Example 1:

Input: nums =  [1,2,3],
Output: [1,2] or [1,3]
Example 2:

Input: nums = [1,2,4,8],
Output: [1,2,4,8]
Tags
Dynamic Programming/DP
Coordinate DP
Company
Google
Related Problems
76
Longest Increasing Subsequence
Medium

    @param nums: a set of distinct positive integers
    @return: the largest subset
    """
    def largestDivisibleSubset(self, nums):
        pass