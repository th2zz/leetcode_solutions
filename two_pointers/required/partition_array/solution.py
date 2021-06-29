class Solution:
    """
    Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

All elements < k are moved to the left
All elements >= k are moved to the right
Return the partitioning index, i.e the first index i nums[i] >= k.
Example
Example 1:

Input:

nums = []
k = 9
Output:

0
Explanation:

Empty array, print 0.

Example 2:

Input:

nums = [3,2,2,1]
k = 2
Output:

1
Explanation:

the real array is[1,2,2,3].So return 1.

Challenge
Can you partition the array in-place and in O(n)O(n)?
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def partitionArray(self, nums, k):
        if not nums:
            return 0
        start, end = 0, len(nums) - 1
        # 没有必要去取pivot index并交换至末尾了因为不需要 pivot在中间 也不需要他的index 只需要满足 left half < k; right half >= k
        # pivot_index = (start + end) // 2
        # self.swap(nums, pivot_index, end)
        pivot = k
        i, j = start, start
        # end + 1 因为pivot不在末尾了
        for j in range(start, end + 1):
            if nums[j] < pivot:
                # [< pivot i][ >= pivot]
                self.swap(nums, i, j)
                # i goes to next to-be-swapped pos
                i += 1
        # [< pivot][i >= pivot]
        # 这里也没有必要了 因为pivot都不在末尾了
        # self.swap(nums, i, end)
        return i


# print(Solution().partitionArray([3,2,1], 2))
# 同向双指针partition法的一个变种 具体就是不需要取pivot了(当然也就不需要把pivot移动到末尾) 直接用给定的k  j的遍历range注意不再是去掉末尾的range 而是整个range
# 根据invariant 最后i的位置即右半>=pivot开始位置