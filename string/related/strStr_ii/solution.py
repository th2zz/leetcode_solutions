class Solution:
    """https://www.lintcode.com/problem/594/?_from=collection&fromId=161
    Description
Implement strStr function in O(n + m) time.

strStr return the first index of the target string in a source string. The length of the target string is m and the length of the source string is n.
If target does not exist in source, just return -1.

Example
Example 1:

Input：source = "abcdef"， target = "bcd"
Output：1
Explanation：
The position of the first occurrence of a string is 1.
Example 2:

Input：source = "abcde"， target = "e"
Output：4
Explanation：
The position of the first occurrence of a string is 4.
Tags
String
    @param: source: A source string
    @param: target: A target string
    @return: An integer as index
    """
    def strStr2(self, source, target):
        if source is None or target is None:
            return -1
        if target == "":
            return 0
        BASE = 1000000
        m, n = len(target), len(source)
        power = 1
        # 31^m
        for i in range(m):
            power = (power * 31) % BASE
        # target
        target_code = 0
        for i in range(m):
            target_code = (target_code * 31 + ord(target[i])) % BASE
        hash_code = 0
        for i in range(n):
            #  abc +d
            hash_code = (hash_code * 31 + ord(source[i])) % BASE
            # 不够m个字符 继续
            if i < m - 1:
                continue
            elif i >= m:
                # abcd -a
                #    i
                hash_code = (hash_code - ord(source[i - m]) * power) % BASE
                if hash_code < 0:
                    hash_code += BASE
            if hash_code == target_code:
                if source[i - m + 1:i + 1] == target:
                    return i - m + 1
        return -1
