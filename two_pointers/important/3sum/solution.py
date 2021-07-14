class Solution:
    """
    Description
    Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

    Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)

    The solution set must not contain duplicate triplets.

    Example
    Example 1:

    Input:

    numbers = [2,7,11,15]
    Output:

    []
    Explanation:

    Cannot find triples such that the sum of three numbers is 0.
    Example 2:

    Input:

    numbers = [-1,0,1,2,-1,-4]
    Output:

    [[-1, 0, 1],[-1, -1, 2]]
    Explanation:

    [-1, 0, 1] and [-1, -1, 2] are two triples.1, 2]]
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, numbers):
        # O(n^2 + NlogN) time overall O(k) space k=#solutions
        # 输入没有排好序 不考虑重复
        if not numbers or len(numbers) < 3:
            return []
        numbers = sorted(numbers)
        # 锚定/遍历三元组中的最小值 起始位置
        results = []
        for i in range(0, len(numbers) - 2):
            # 和左边一样=考虑过了 跳过  eliminate duplicates
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            # i is first element in triple, find two sum数组起始位置为i + 1
            left, right, target = i + 1, len(numbers) - 1, -numbers[i]
            # 带有去重逻辑的two sum
            self.find_two_sum_unique_pairs(numbers, left, right, target, results)
        return results

    def find_two_sum_unique_pairs(self, numbers, left, right, target, results):
        # 原来的解left, right = 0, len(nums) - 1    没有results参数
        # O(n)
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                # count += 1
                results.append([-target, numbers[left], numbers[right]])
                right -= 1
                left += 1
                # eliminate duplicates
                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1
                while left < right and numbers[right] == numbers[right + 1]:
                    right -= 1
            elif sum > target:
                right -= 1
            else:
                left += 1


