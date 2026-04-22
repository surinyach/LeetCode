class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        mappings_s = {}
        mappings_t = {}

        for i in range(len(s)):
            if not s[i] in mappings_s:
                mappings_s[s[i]] = t[i]
            else:
                if not mappings_s[s[i]] == t[i]:
                    return False
                
            if not t[i] in mappings_t:
                mappings_t[t[i]] = s[i]
            else:
                if not mappings_t[t[i]] == s[i]:
                    return False

        return True

        # Being n = len(s) = len(t)
        # Time Complexity: O(n)
        # Space Complexity: O(n + n) -> O(n)