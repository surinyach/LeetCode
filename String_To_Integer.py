class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        MAX32_BIT = 2**31
        res = 0
        negative = False
        number = False

        for c in s:
            if c == "-" and not number:
                negative = True
                number = True
            elif c == "+" and not number:
                number = True
            elif c == " " and not number:
                continue
            elif c >= "0" and c <= "9":
                res *= 10
                n = ord(c) - ord("0")
                res += n
                number = True
            else: 
                break
    
        if res >= MAX32_BIT and not negative:
            res = MAX32_BIT - 1
        elif res > MAX32_BIT and negative:
            res = MAX32_BIT
        return res if not negative else res*-1