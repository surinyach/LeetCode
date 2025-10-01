class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = strs[0][:len(strs[0])]
        for i in range(1, len(strs)):
            curr = strs[i]
            lcurr = len(curr)
            lres = len(res)
            lmax = lcurr if lcurr > lres else lres
            lmin = lcurr if lcurr < lres else lres 
            for j in range(0, lmax):
                if j >= lmin or curr[j] != res[j]:
                    res = res[:j]
                    break
        
        return res