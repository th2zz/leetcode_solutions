# 1. two sum

brute force O(n^2) O(1)

optimal O(n) O(n)  speed up **finding the counterpart** by keeping a record of what has been seen in a dict, when we see the counterpart, the counterpart of the counterpart is already seen, thus we are done, when we haven't seen it, we keep the record of current item.

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [i, d[target - num]]
            d[num] = i
```



# 2. add two numbers

n = length of l1, m = length l2

O(n+m) O(n+m)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
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
```

simulate a half adder = O(max(n, m)) O(max(n, m)), but not good for production code



# 3. longest substring without repeating characters

brute force do it by looping O(n^2) O(1)

invariant: r指针第一轮后始终位于之前匹配的最长无重复子串的最后一个字符

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited, n = set(), len(s)
        
        r, ans = -1, 0
        for l in range(n):
            if l != 0:
                
                visited.remove(s[l - 1])
            while r + 1 < n and s[r + 1] not in visited:
                
                visited.add(s[r + 1])
                r += 1
            # temporary result: start from index l to r
            ans = max(ans, r - l + 1)
        return ans
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        visited = set()
        res = 0
        r = -1
        for l in range(n):
            # 左指针只有第二轮才开始向右移动一格，移除前一个字符 代表此时的新起始位置
            if l != 0:
                visited.remove(s[l - 1])
            # keep matching next unique char, advance right pointer to the unique char
            while r + 1 < n and s[r + 1] not in visited:
                visited.add(s[r + 1])
                r += 1
            # temporary result: start from index l to r
            res = max(res, r - l + 1)
        return res
```

