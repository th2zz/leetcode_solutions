class Solution:
    # @param {int[]} A an array
    # @return {int} total of reverse pairs
    def reversePairs(self, A):
        # Write your code here
        self.tmp = [0 for _ in range(len(A))]
        return self.merge_sort(A, 0, len(A) - 1)

    def merge_and_count(self, A, start, end, mid, cnt):
        left, right, index = start, mid + 1, start
        while left <= mid and right <= end:
            if A[left] > A[right]:
                self.tmp[index] = A[right]
                right += 1
                # add count! left sublist中[left,mid] 都和right构成逆序对 批量计数
                cnt += mid - left + 1
            else:
                self.tmp[index] = A[left]
                left += 1
            index += 1
        while left <= mid:
            self.tmp[index] = A[left]
            index += 1
            left += 1
        while right <= end:
            self.tmp[index] = A[right]
            index += 1
            right += 1
        for left in range(start, end + 1):
            A[left] = self.tmp[left]
        return cnt

    def merge_sort(self, A, start, end):
        if start >= end:
            return 0
        mid = (start + end) // 2
        # 先递归数两边 再于merge环节中数横跨左右的  横跨左右逆序对判断条件为 = A[left] > A[right]
        left_count = self.merge_sort(A, start, mid)
        right_count = self.merge_sort(A, mid + 1, end)
        total_count = self.merge_and_count(A, start, end, mid, left_count + right_count)
        return total_count

# print(Solution().reversePairs([2,4,1,3,5]))

