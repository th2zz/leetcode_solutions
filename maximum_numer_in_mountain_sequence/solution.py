class Solution:
    """
    Description
Given a mountain sequence of n integers which increase firstly and then decrease, find the mountain top(Maximum).

Arrays are strictly incremented, strictly decreasing

Example
Example 1:

Input: nums = [1, 2, 4, 8, 6, 3]
Output: 8
Example 2:

Input: nums = [10, 9, 8, 7],
Output: 10
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < nums[mid + 1]:
                start = mid
            elif nums[mid] > nums[mid + 1]:
                end = mid
            elif nums[mid] == nums[mid + 1]:
                start = mid
        return max(nums[start], nums[end])

print(Solution().mountainSequence([1, 2, 4, 8, 6, 3]))
print(Solution().mountainSequence([10, 9, 8, 7]))

