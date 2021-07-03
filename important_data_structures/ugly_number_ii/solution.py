import heapq


class Solution:
    """https://www.lintcode.com/problem/4/?_from=collection&fromId=161
    Description
Ugly number is a number that only have prime factors 2, 3 and 5.

Design an algorithm to find the Nth ugly number. The first 10 ugly numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12...

Note that 1 is typically treated as an ugly number.

1 \leq n \leq 10^{5}1≤n≤10
5


Example
Example 1:

Input:

n = 9
Output:

10
Explanation:

[1,2,3,4,5,6,8,9,10,....],the ninth ugly number is 10.

Example 2:

Input:

n = 1
Output:

1
Challenge
O(n log n) or O(n) time.

Tags
Dynamic Programming/DP
Heap
Mathmatics
Related Problems
518
Super Ugly Number
Medium
517
Ugly Number
Easy
    @param n: An integer
    @return: return a  integer as description.
    """

    def nthUglyNumber(self, n):
        heap = [1]  # keep ugly numbers
        seen = set([1])  # visited set
        curr_ugly = 1
        for _ in range(n):
            curr_ugly = heapq.heappop(heap)  # 如果是最后一个丑数 不需要把乘积放到heap
            for factor in [2, 3, 5]:
                new_ugly = curr_ugly * factor
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        return curr_ugly
