class Solution:
    """
    https://www.lintcode.com/problem/75/?_from=ladder&fromId=161
    A[0] < A[1] && A[A.length - 2] > A[A.length - 1]. 两边向中间升
    It's guaranteed the array has at least one peak.
    The array may contain multiple peeks, find any of them.
    The array has at least 3 numbers in it.

    @param A: An integers array.
    @return: return any of peek positions.
    """

    def findPeak(self, A):
        # peak不能在两端 所以在[1, len(A) - 2]查找
        start, end = 1, len(A) - 2
        while start + 1 < end:
            mid = (start + end) // 2
            # 如果mid向左上方倾斜 搜索左半边
            if A[mid] < A[mid - 1]:
                end = mid
            # 如果mid向右上方倾斜 搜索右半边
            elif A[mid] < A[mid + 1]:
                start = mid
            # mid为peak
            else:
                return mid
        # 因为保证一定有peak, 返回start end中较大的那个
        return end if A[start] < A[end] else start
