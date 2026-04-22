class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        for i in range(0, len(str_x) // 2):
            if str_x[i] != str_x[len(str_x) - 1 - i]:
                return False
            
        return True