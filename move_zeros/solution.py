class Solution:
    """
    0丢到数组末尾
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes_naive(self, nums):
        fill_ptr = 0
        for move_ptr in range(len(nums)):
            if nums[move_ptr] != 0:
                # 不等于才有交换意义
                if fill_ptr != move_ptr:
                    nums[fill_ptr], nums[move_ptr] = nums[move_ptr], nums[fill_ptr]
                fill_ptr += 1

    def moveZeroes(self, nums):
        # minimize write operations by not swapping
        fill_ptr = 0
        for move_ptr in range(len(nums)):
            if nums[move_ptr] != 0:
                if fill_ptr != move_ptr:
                    nums[fill_ptr] = nums[move_ptr]
                fill_ptr += 1
        # 把后续所有数字清零
        for fill_ptr in range(fill_ptr, len(nums)):
            if nums[fill_ptr] != 0:
                nums[fill_ptr] = 0
