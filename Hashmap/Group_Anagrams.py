class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}
        anagrams = []

        for s in strs:
            key = [0]*26
            for c in s:
                key[ord(c) - 97] += 1
            # A tuple is an immutable sequence that can be used as a key in dictionaries or sets
            key = tuple(key)
            if key not in groups:
                groups[key] = [s]
            else:
                groups[key].append(s)
        
        for k in groups:
            anagrams.append(groups[k])

        return anagrams

        # Time Complexity: O(n * m), where n = len(strs) and m = len(strs[i])
        # Space Complexity: O(n * m), where n = len(strs) and m = len(strs[i])
            # The worst space case happens when there is not a single pair of words that form an anagram in strs