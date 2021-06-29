# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        simulate a half adder = O(max(n, m)) O(max(n, m)), but not good for production code
        n = length of l1, m = length l2
        O(n+m) O(n+m)
        Args:
            l1 ():
            l2 ():

        Returns:

        """
        num1 = ''
        num2 = ''
        while l1:
            num1 = str(l1.val) + num1
            l1 = l1.next
        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next
        res = str(int(num1) + int(num2))
        head = ListNode(-1)
        p = head
        for i in reversed(res):
            p.next = ListNode(int(i))
            p = p.next
        return head.next


