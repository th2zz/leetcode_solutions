class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        visited = set()
        res, r = 0, 0
        for l in range(n):
            if l != 0:
                visited.remove(s[l - 1])
            while r in range(n) and s[r] not in visited:
                visited.add(s[r])
                r += 1
            res = max(res, r - l)
        return res



