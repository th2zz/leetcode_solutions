class Solution:
    """https://www.lintcode.com/problem/138/?_from=collection&fromId=161
    Description
Given an integer array, find a subarray where the sum of numbers is zero. Your code should return the index of the first number and the index of the last number.

There is at least one subarray that it's sum equals to zero.

Example
Example 1:

Input:  [-3, 1, 2, -3, 4]
Output: [0, 2] or [1, 3].
Explanation: return anyone that the sum is 0.
Example 2:

Input:  [-3, 1, -4, 2, -3, 4]
Output: [1,5]
Tags
Hash Table
Prefix Sum Array
Array

Related Problems
405
Submatrix Sum
Medium
404
Subarray Sum II
Medium
406
Minimum Size Subarray Sum
Medium
139
Subarray Sum Closest
Medium

    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number that sums to 0
    """

    # at pos i, prefix a + ... + b already seen
    # a + ... + b + c + ... + nums[i] = a + ... + b  <=>  c + ... + nums[i] = 0
    # then we return [index of c, i]
    def subarraySum(self, nums):
        d = {0: -1}  # prefix sum -> index
        prefix_sum = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            if prefix_sum in d:
                return [d[prefix_sum] + 1, i]
            d[prefix_sum] = i
        return [-1, -1]


nums = [-3, 1, 2, -3, 4]
print(Solution().subarraySum(nums))
nums = [-3, 1, -4, 2, -3, 4]
print(Solution().subarraySum(nums))