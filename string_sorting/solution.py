class Solution:
    """
    https://www.lintcode.com/problem/string-sorting/
    @param s: string
    @return: sort string in lexicographical order
    """
    def swap(self, left, right, strings):
        tmp = strings[left]
        strings[left] = strings[right]
        strings[right] = tmp

    def sorting(self, s):
        # reduce the problem to standard quick sorting
        strings = s.split(',')
        self.qsort(0, len(strings) - 1, strings)
        return ','.join(strings)

    def partition(self, start, end, strings):
        left, right = start, end
        pivot = strings[(left + right) // 2]
        while left <= right:
            while left <= right and strings[left] < pivot:
                left += 1
            while left <= right and strings[right] > pivot:
                right -= 1
            if left <= right:
                # swap this pair of inversion
                self.swap(left, right, strings)
                left += 1
                right -= 1
        return left, right

    def qsort(self, start, end, strings):
        if start >= end:
            return
        # use separate variables to preserve original information
        left, right = self.partition(start, end, strings)
        # 此时 two sublists = [start...right][left...end]
        self.qsort(start, right, strings)
        self.qsort(left, end, strings)


res = Solution().sorting("bb,aa,lintcode,c")
print(res)
