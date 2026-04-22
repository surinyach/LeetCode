class Solution(object):
    def isPalindrome(self, x):
        number = str(x)
        length = len(number)

        first = 0
        last = length - 1

        for i in range(0,length/2):
            if number[first] != number[last]:
                return False
            
            first += 1
            last -= 1
        
        return True