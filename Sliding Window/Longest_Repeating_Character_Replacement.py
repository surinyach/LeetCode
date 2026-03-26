class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        longest = 0
        l = 0
        counts = [0] * 26 # Counts of the amount of specific letters inside the window

        for r in range(len(s)):
            counts[ord(s[r]) - 65] += 1
            while (r - l + 1) - max(counts) > k:
                counts[ord(s[l]) - 65] -= 1
                l += 1
            
            longest = max(longest, (r-l+1))

        return longest