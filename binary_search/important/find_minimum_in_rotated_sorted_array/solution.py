class Solution:
    """
    Description
Suppose a sorted array in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You can assume no duplicate exists in the array.

Example
Example 1:

Input：[4, 5, 6, 7, 0, 1, 2]
Output：0
Explanation：
The minimum value in an array is 0.
Example 2:

Input：[2,1]
Output：1
Explanation：
The minimum value in an array is 1.

    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            # 说明mid取在了大的部分 舍弃左半边
            if nums[mid] > nums[end]:
                start = mid
            # mid取在了小的部分 move右边界
            elif nums[mid] <= nums[end]:
                end = mid
        return min(nums[start], nums[end])

