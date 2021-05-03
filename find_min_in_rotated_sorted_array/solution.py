class Solution:
    """旋转数组最小值
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

