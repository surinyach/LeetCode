class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        for i in range (0, n):
            div3 = (i + 1) % 3 == 0
            div5 = (i + 1) % 5 == 0

            if div3 and div5:
                result.append("FizzBuzz")
            elif div3:
                result.append("Fizz")
            elif div5:
                result.append("Buzz")
            else:
                result.append(str(i + 1))
        
        return result