class Solution:
    """
    https://www.lintcode.com/problem/976/

    给了4个数组 每组里选1个数 使得4sum to 0, find #solutions

    - input not sorted
    - input has duplicates
    - no need to eliminate duplicate answer
    @param A: a list
    @param B: a list
    @param C: a list
    @param D: a list
    @return: how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero
    """

    def fourSumCount(self, A, B, C, D):
        # 本题类似two sum iii data structure design
        # - 维护一个ab和出现频次的map
        # - 遍历所有可能cd和的counterpart  cnt累加其在 map中的频次
        table = {}
        for a in A:
            for b in B:
                total = a + b
                table[total] = table.get(total, 0) + 1
        cnt = 0
        for c in C:
            for d in D:
                total = c + d
                cnt += table.get(-total, 0)
        return cnt
