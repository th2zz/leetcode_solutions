class Solution:
    """https://www.lintcode.com/problem/76/?_from=collection&fromId=161
    Algorithms
Medium
Accepted Rate
37%

DescriptionSolutionNotesDiscussLeaderboard
Description
Given a sequence of integers, find the longest increasing subsequence (LIS).

You code should return the length of the LIS.

What's the definition of longest increasing subsequence?

The longest increasing subsequence problem is to find a subsequence of a given sequence in which the subsequence's elements are in sorted order, lowest to highest, and in which the subsequence is as long as possible. This subsequence is not necessarily contiguous, or unique.

https://en.wikipedia.org/wiki/Longest_increasing_subsequence

Example
Example 1:

Input:

nums = [5,4,1,2,3]
Output:

3
Explanation:

LIS is [1,2,3]
Example 2:

Input:

nums = [4,2,4,5,3,7]
Output:

4
Explanation:

LIS is [2,4,5,7]

Challenge
Time complexity O(n^2)O(n
2
 ) or O(nlogn)O(nlogn)

Tags
Dynamic Programming/DP
Coordinate DP
Related Problems
1645
Least Subsequences
Medium
1111
Maximum Length of Pair Chain
Medium
1093
Number of Longest Increasing Subsequence
Medium
602
Russian Doll Envelopes
Hard
603
Largest Divisible Subset
Medium
622
Frog Jump
Hard
    what is subsequence: subsequence does not have to be contiguous
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
