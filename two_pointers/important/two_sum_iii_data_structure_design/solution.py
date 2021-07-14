class TwoSum:
    """
    This naive solution will exceed timeout limit
    Description
    Design and implement a TwoSum class. It should support the following operations: add and find.

    add - Add the number to an internal data structure.
    find - Find if there exists any pair of numbers which sum is equal to the value.

    Example
    Example 1:

    add(1); add(3); add(5);
    find(4) // return true
    find(7) // return false
    """
    def __init__(self):
        self.nums = []
    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        self.nums.append(number)
        index = len(self.nums) - 1
        while index >= 1 and self.nums[index - 1] > self.nums[index]:
            self.nums[index], self.nums[index - 1] = self.nums[index - 1], self.nums[index]
            index -= 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        left, right = 0, len(self.nums) - 1
        while left < right:
            sum = self.nums[left] + self.nums[right]
            if sum > value:
                right -= 1
            elif sum < value:
                left += 1
            elif sum == value:
                return True
        return False
#
# a = TwoSum()
# a.add(1)
# a.add(3)
# a.add(5)
# print(a.nums)
# print(a.find(4))
# print(a.find(7))