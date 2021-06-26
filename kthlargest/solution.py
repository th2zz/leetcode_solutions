class Solution:
    """ O(n) O(1)
    @param k: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def quick_select(self, nums, start, end, k):
        # quick select k-th smallest element
        pivot_index = self.partition(nums, start, end)
        if k - 1 == pivot_index:
            return nums[pivot_index]
        elif k - 1 < pivot_index:
            return self.quick_select(nums, start, pivot_index - 1, k)
        else:
            return self.quick_select(nums, pivot_index + 1, end, k)

    def kthLargestElement(self, k, nums):
        if not nums:
            return -1
        if k > len(nums):
            return -1
        # k-th largest = "len(nums) + 1 - k"-th smallest
        return self.quick_select(nums, 0, len(nums) - 1, len(nums) + 1 - k)

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def partition(self, nums, start, end):
        # or with randint [a,b] randrange [a, b)
        pivot_index = (start + end) // 2
        pivot = nums[pivot_index]
        self.swap(nums, pivot_index, end)
        i = start
        for j in range(start, end):
            if nums[j] < pivot:
                self.swap(nums, i, j)
                i += 1
        self.swap(nums, i, end)
        return i

