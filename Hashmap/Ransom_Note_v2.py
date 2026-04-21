class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if len(ransomNote) > len(magazine):
            return False
        
        ransomLetters = [0] * 26

        for i in range(len(ransomNote)):
            ransomLetters[ord(ransomNote[i] - 97)] += 1
           
        for i in range(len(magazine)):
            ransomLetters[ord(magazine[i]) - 97] -= 1
            if ransomLetters[ord(magazine[i]) - 97] < 0:
                return False

        return True
    
    # Time complexity: O(len(magazine) + len(ransomNote))
    # Space complexity: O(1)