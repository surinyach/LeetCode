from collections import deque

class Solution(object):
    def _expand(self, l, r, s):
        sub_len = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            sub_len += 1
            l -= 1
            r += 1
        return sub_len

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None: 
            return ""
        
        max_len = 0
        l = 0
        r = 0

        for i in range(0, len(s)):
            sublen1 = self._expand(i - 1, i, s)
            sublen2 = self._expand(i, i, s) - 1
            
            if sublen2 >= max_len:
                max_len = sublen2
                l = i - sublen2
                r = i + sublen2 
            if sublen1 > max_len:
                max_len = sublen1
                l = i - sublen1
                r = i + sublen1 - 1
        
        return s[l:r + 1]