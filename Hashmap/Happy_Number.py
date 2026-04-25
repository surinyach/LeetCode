class Solution:
    def isHappy(self, n: int) -> bool:
        sums = set()
        while n not in sums:
            n_sum = 0
            sums.add(n)
            while n > 0:
                n_sum += (n % 10)**2
                n = n // 10
            n = n_sum
            if n == 1:
                return True
        return False
    
    # Time Complexity: O(log n)
        #   Each step computes the sum of squares of digits → O(log n)
        #   The number of steps is bounded since values quickly fall into a small cycle

    # Space Complexity: O(1)
        #   The set stores previously seen values, but the total number of possible values is bounded