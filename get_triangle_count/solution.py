class Solution:
    """
    382 · Triangle Count
    Algorithms
    Medium
    Accepted Rate
    41%

    Description
    Given an array of integers, how many three numbers can be found in the array, so that we can build an triangle 
    whose three edges length is the three numbers that we find?

    Example
    Example 1:

    Input: [3, 4, 6, 7]
    Output: 3
    Explanation:
    They are (3, 4, 6),
             (3, 6, 7),
             (4, 6, 7)
    Example 2:

    Input: [4, 4, 4, 4]
    Output: 4
    Explanation:
    Any three numbers can form a triangle.
    So the answer is C(3, 4) = 4
    @param S: A list of integers
    @return: An integer
    """

    def triangleCount(self, S):
        # O(N^2 + NlogN) O(1)
        if not S:
            return 0
        S.sort()  # 必须的因为我们要复用双指针求two sum的解
        # 遍历最大边索引位置 最大边左边寻找两个小边 two_sum
        ans = 0
        for i in range(2, len(S)):
            ans += self.get_triangle_count(S, i)
        return ans

    def get_triangle_count(self, nums, target_index):
        """ 找到target_index 左边  两数之和为target_sum的组合的个数
        """
        # 寻找范围[0, target_index - 1]
        left = 0
        right = target_index - 1
        target_sum = nums[target_index]
        total = 0
        while left < right:
            # 小边之和大于大边
            if nums[left] + nums[right] > target_sum:
                # 一次求出多个可行解的个数 从left 到 right - 1都是满足条件的对 共right - left个
                total += right - left
                right -= 1  # 已经计入right所有可能的情况 减少sum查看下一个right
            else:  # 不够 需要增大sum move left
                left += 1
        return total
