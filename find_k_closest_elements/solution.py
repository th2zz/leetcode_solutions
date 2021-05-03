class Solution:
    """
    Description
    Given target, a non-negative integer k and an integer array A sorted in ascending order, find the k closest numbers
    to target in A, sorted in ascending order by the difference between the number and target.
    Otherwise, sorted in ascending order by number if the difference is same.

    The value k is a non-negative integer and will always be smaller than the length of the sorted array.
    Length of the given array is positive and will not exceed 10^410
    ​4
    ​​
    Absolute value of elements in the array will not exceed 10^410
    ​4
    ​​
    Example
    Example 1:

    Input: A = [1, 2, 3], target = 2, k = 3
    Output: [2, 1, 3]
    Example 2:

    Input: A = [1, 4, 6, 8], target = 3, k = 3
    Output: [4, 1, 6]
    Challenge
    O(logn + k) time
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # target可以在A中也可以不在   找到最接近target的两个数
        right = self.findLeastUpperBound(A, target)
        left = right - 1
        # 两根指针背向而行 merge sorted array直到找到k个数为止; 此处判断有序标准为 "距离target是否更近"
        results = []
        for _ in range(k):
            # 左边更接近(小) 选左边
            if self.isLeftCloser(A, target, left, right):
                results.append(A[left])
                left -= 1
            else:
                results.append(A[right])
                right += 1
        return results

    def isLeftCloser(self, A, target, left, right):
        # idempotent for corner cases 如果左边已经耗尽 返回false
        if left < 0:
            return False
        # 右边已经耗尽 返回true 从此开始只append左边
        if right >= len(A):
            return True
        # 如果左右距离相等  选左边
        return target - A[left] <= A[right] - target

    def findLeastUpperBound(self, A, target):
        # find least upperbound
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            # mid >= target, mid符合条件 向左边去寻找
            # 答案在mid及其左边 丢掉右边
            if A[mid] >= target:
                end = mid
            # 如果mid < target, >= target的元素在mid右边 丢掉mid左边
            else:
                # 这里也可以mid + 1
                start = mid
        # 因为需要找最左数 这里先判断start
        if A[start] >= target:
            return start
        if A[end] >= target:
            return end
        return len(A)
