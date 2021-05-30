# Input: nums = [2, 7, 11, 15], target = 24.
# Output: 5.
# Explanation:
# 2 + 7 < 24
# 2 + 11 < 24
# 2 + 15 < 24
# 7 + 11 < 24
# 7 + 15 < 24

# Input: nums = [1], target = 1.
# Output: 0.


class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    naive brute force takes O(n^2) two pass
    O(nlogn) O(1)
    """
    def twoSum5(self, nums, target):
        nums.sort()
        count, left, right = 0, 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1 # decrease sum
            else:
                count += right - left # index @ left+1, ..., right all satisify the condition
                left += 1 # increase sum
        return count
