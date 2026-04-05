class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = 0
        for i in digits:
            number *= 10
            number += i
        number += 1
        sol = []
        while number > 0:
            n = number % 10
            sol = [n] + sol
            number /= 10
        return sol