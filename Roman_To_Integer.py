class Solution(object):

    def before(self, anterior, char):
        if anterior == 'I':
            if char == 'V':
                return 3
            if char == 'X':
                return 8
        elif anterior == 'X':
            if char == 'L':
                return 30
            if char == 'C':
                return 80
        elif anterior == 'C':
            if char == 'D':
                return 300
            if char == 'M':
                return 800
        return 0

    
    def romanToInt(self, s):

        number = 0
        roman = {
            'I': 1,
            'V': 5,
            'X': 10, 
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        anterior = ''
        for char in s:
            if anterior in ['I', 'X', 'C']:
                res = self.before(anterior, char)
                if res != 0:
                    number += res
                else:
                    number += roman[char]
            else:
                number += roman[char]
            anterior = char
        
        return number