class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = []
        res = 0
        for c in s:
            if c in chars:
                if res < len(chars):
                    res = len(chars)
                i = chars.index(c)
                del chars[:i + 1]
            chars.append(c)
            
        return res if res > len(chars) else len(chars)