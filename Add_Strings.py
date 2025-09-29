class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        carry = False
        i = len(num1) - 1
        j = len(num2) - 1
        result = ""
        
        while i >= 0 or j >= 0 or carry:
            current = 0
            if i >= 0:
                current += ord(num1[i]) - ord("0")
                i -= 1
            if j >= 0:
                current += ord(num2[j]) - ord("0")
                j -= 1
            if carry:
                current += 1
                carry = False
            if current >= 10:
                current = current % 10
                carry = True
            
            current += ord("0")
            result = chr(current) + result
        
        return result