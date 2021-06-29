class Solution:
    """https://www.lintcode.com/problem/14/?_from=collection&fromId=161
    Description
Given a sorted array (ascending order) and a target number, find the first index of this number in O(log n)O(logn) time complexity.

If the target number does not exist in the array, return -1.

Example
Example 1:

Input:

tuple = [1,4,4,5,7,7,8,9,9,10]
target = 1
Output:

0
Explanation:

The first index of 1 is 0.

Example 2:

Input:

tuple = [1, 2, 3, 3, 4, 5, 10]
target = 3
Output:

2
Explanation:

The first index of 3 is 2.

Example 3:

Input:

tuple = [1, 2, 3, 3, 4, 5, 10]
target = 6
Output:

-1
Explanation:

There is no 6 in the array，return -1.
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
            else:
                end = mid
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        return -1

print(Solution().binarySearch([1,4,4,5,7,7,8,9,9,10], 1))
print(Solution().binarySearch([1, 2, 3, 3, 4, 5, 10], 3))

