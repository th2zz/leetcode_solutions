class Solution:
    from math import inf
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 小的在前
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        x, y = len(nums1), len(nums2)
        low, high = 0, x
        even_len = (x + y) % 2 == 0
        while low <= high:
            lx_len = int((low + high) / 2)
            ly_len = int((x + y + 1) / 2 - lx_len)
            lx_max = -inf if lx_len == 0 else nums1[lx_len - 1]
            ly_max = -inf if ly_len == 0 else nums2[ly_len - 1]
            rx_min = inf if lx_len == x else nums1[lx_len]
            ry_min = inf if ly_len == y else nums2[ly_len]
            # 交叉比较 确定是否达到invariant 左半<=右半
            if lx_max <= ry_min and ly_max <= rx_min:
                if even_len:
                    return (max(lx_max, ly_max) + min(rx_min, ry_min)) / 2
                else:
                    return max(lx_max, ly_max)
            # lx_max大了 去x的左半查找 否则 去x的右半查找
            elif lx_max > ry_min:
                high = lx_len - 1
            elif ly_max > rx_min:
                low = lx_len + 1
        return -1



