class Solution:
    """https://www.lintcode.com/problem/685/?_from=collection&fromId=161
    Description
Given a continuous stream of data, write a function that returns the first unique number (including the last number) when the terminating number arrives. If the terminating number is not found, return -1.

Example
Example1

Input:
[1, 2, 2, 1, 3, 4, 4, 5, 6]
5
Output: 3
Example2

Input:
[1, 2, 2, 1, 3, 4, 4, 5, 6]
7
Output: -1
Example3

Input:
[1, 2, 2, 1, 3, 4]
3
Output: 3
    @param nums: a continuous stream of numbers
    @param number: the terminating number
    @return: returns the first unique number
    """

    def firstUniqueNumber(self, nums, number):
        if not nums:
            return -1
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            if num == number:
                break
        else:
            return -1  # terminating number not found
        for num in nums:
            if counter[num] == 1:
                return num
            # 这段代码可以没有 if terminate number not found already returned,
            # found and > 1 times is not possible because of first break
            # found and == 1 times already returned in the above if
            if num == number:
                break
        return -1
