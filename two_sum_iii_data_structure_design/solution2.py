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
        self.num_to_cnt_map = {}
    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        self.num_to_cnt_map[number] = self.num_to_cnt_map.get(number, 0) + 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        for num1 in self.num_to_cnt_map.keys():
            num2 = value - num1
            num2cnt = 2 if num1 == num2 else 1
            if self.num_to_cnt_map.get(num2, 0) >= num2cnt:
                return True
        return False


# a = TwoSum()
# a.add(1)
# a.add(3)
# a.add(5)
# print(a.find(4))
# print(a.find(7))