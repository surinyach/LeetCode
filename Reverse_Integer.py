class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        if x < 0:
            negative = True
        
        x = abs(x)
        str_num = list(str(x))
        str_len = len(str_num)

        for i in range(0, str_len // 2):
            end = str_len - 1 - i
            aux = str_num[i]
            str_num[i] = str_num[end]
            str_num[end] = aux
        
        x = int("".join(str_num))
        if x > 2**31: return 0
        return -x if negative else x