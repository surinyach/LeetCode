class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        pattern_matches = {}
        s_matches = {}
        for i in range(len(pattern)):
            if words[i] not in s_matches:
                s_matches[words[i]] = pattern[i]
            else:
                if s_matches[words[i]] != pattern[i]:
                    return False

            if pattern[i] not in pattern_matches:
                pattern_matches[pattern[i]] = words[i] 
            else:
                if pattern_matches[pattern[i]] != words[i]:
                    return False
                                
        return True
    
    # Time Complexity = O(n), being n = len(pattern) = len(words in s)
    # Space Complexity = O(n), being n = number of different words in s = number of different letters in pattern