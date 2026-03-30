class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        nicest_substring = ""
        substrings = []
        for i in range(0, len(s)):
            substring = s[i]
            for j in range(i + 1, len(s)):
                substring += s[j]
                substrings.append(substring)
                
        for s in substrings:
            letters = set(s)
            is_nice = True
            for i in range(0, len(s)):
                if chr(ord(s[i]) + 32) in letters or chr(ord(s[i]) - 32) in letters:
                    continue
                else:
                    is_nice = False
                    break
                    
            if is_nice and len(s) > len(nicest_substring):
                nicest_substring = s

        return nicest_substring