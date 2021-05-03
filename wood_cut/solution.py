class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        if not L:
            return 0
        start, end = 1, min(max(L), sum(L) // k)
