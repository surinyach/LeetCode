import re

class Solution:
    # String python replace method
    #   Replace a specific phrase with another specific phrase
    #   x = txt.replace("bananas", "apples")

    # String python regex with re package
    #   re.sub() method replaces specific patterns of a string for other desired characters
    #   re.sub(pattern, replace, string)
    #   Non-Alphanumeric regex in python: '[^0-9a-zA-Z]+':
    #       [] -> match any one character inside the brackets
    #       ^ -> When this symbol is the first one inside the brackets, it means NOT
    #       0-9 -> Matches any digit
    #       a-z -> Matches any lowercase letter
    #       A-Z -> Matches any uppercase letter
    #       + -> This symbol means one ormore consecutive characters that fit the pattern

    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^0-9a-zA-Z]+', "", s)
        s = s.lower()
        words = s.split()
        s = "".join(words)
        return s == s[::-1]