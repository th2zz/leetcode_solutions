class Solution:
    """https://www.lintcode.com/problem/13/?_from=collection&fromId=161
    Description
For a given source string and a target string, you should output the first index(from 0) of target string in the source string.If the target does not exist in source, just return -1.

Do I need to implement KMP Algorithm in a real interview?

Not necessary. When you meet this problem in a real interview, the interviewer may just want to test your basic implementation ability. But make sure you confirm how to implement with the interviewer first.
Example
Example 1:

Input:

source = "source"
target = "target"
Output:

-1
Explanation:

If the source does not contain the target's content, return - 1.

Example 2:

Input:

source = "abcdabcdefg"
target = "bcd"
Output:

1
Explanation:

If the source contains the target's content, return the location where the target first appeared in the source.

Challenge
O(nm) is acceptable. Can you implement an O(n) algorithm? (hint: KMP)

    O(n^2) brute force best practice  for循环起始位置 一个一个字符比较 等则继续不等抛弃 查看下一个起始位置
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source, target):
        if not target:
            return 0
        for i in range(len(source) - len(target) + 1):
            for j in range(len(target)):
                if source[i + j] == target[j]:
                    if j == len(target) - 1:
                        return i
                else:
                    break
        return -1