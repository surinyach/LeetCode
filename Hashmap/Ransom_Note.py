class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if len(ransomNote) > len(magazine):
            return False
        
        ransomLetters = [0] * 26
        magazineLetters = [0] * 26

        for i in range(len(magazine)):
            if i < len(ransomNote):
                ransomLetters[ord(ransomNote[i]) - 97] += 1
            magazineLetters[ord(magazine[i]) - 97] += 1

        for i in range(len(ransomLetters)):
            if magazineLetters[i] < ransomLetters[i]:
                return False

        return True
    
    # Time complexity: O(n)
    # Space complexity: O(1)