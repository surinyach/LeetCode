class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for c in s:
            letters[c] = letters.get(c, 0) + 1
        
        for c in t:
            if c in letters:
                letters[c] -= 1
            else:
                return False
        
        for l in letters:
            if letters[l] != 0:
                return False
                
        return True
    
    # Time Complexity: O(n + m), where n is the length of s and m is the length of t
    # Space Complexity: O(n), where n is the length of s when all its characters are different