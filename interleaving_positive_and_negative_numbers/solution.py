class Solution:
    """
    https://www.lintcode.com/problem/144/
    Description
    Given an array with positive and negative integers. Re-range it to interleaving with positive and negative integers.

    You are not necessary to keep the original order of positive integers or negative integers.

    Example
    Example 1

    Input : [-1, -2, -3, 4, 5, 6]
    Outout : [-1, 5, -2, 4, -3, 6]
    Explanation :  any other reasonable answer.
    Challenge
    Do it in-place and without extra memory.
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
        # O(n) O(1)
        # 输入是否有序 不是
        # 有没有重复数字 影响不大
        # 已知数据确保正负数相差个数不超过1
        # 不需要额外空间
        # 不需要保持正数和负数原来的顺序
        neg_cnt = self.partition(A)
        pos_cnt = len(A) - neg_cnt
        left = 1 if neg_cnt > pos_cnt else 0
        right = len(A) - (2 if pos_cnt > neg_cnt else 1)
        self.interleave(A, left, right)

    def partition(self, A):
        #  after partition two sublists = [start...right]?[left...end]  left 和 right中间有可能还有一个数, left != right
        left, right = 0, len(A) - 1
        while left <= right:
            while left <= right and A[left] < 0:
                left += 1
            while left <= right and A[right] > 0:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        return left

    def interleave(self, A, left, right):
        while left < right:
            A[left], A[right] = A[right], A[left]
            left, right = left + 2, right - 2
