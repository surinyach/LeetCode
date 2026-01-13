class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        h = 0
        n = len(citations)
        for i in range(0, n):
            c = citations[i]
            if c >= n - i and h < n-i:
                h = n - i
            elif c >= n - i:
                break
        return h