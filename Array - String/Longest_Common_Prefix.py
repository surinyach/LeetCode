class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
    
        prefix = min(strs, key=len)

        for i in range(len(prefix)):
            for word in strs:
                if word[i] != prefix[i]:
                    return prefix[:i]

        return prefix