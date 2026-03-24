class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp = 0
        for c in t:
            if sp == len(s):
                break
            if c == s[sp]:
                sp += 1
        return sp == len(s)