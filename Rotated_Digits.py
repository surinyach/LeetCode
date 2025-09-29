class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        rotations = {0: 0, 1: 1, 8: 8, 2: 5, 5: 2, 6: 9, 9: 6}
        goods = 0
        
        for i in range(1, n + 1):
            aux = i
            good = False
            it = 0
            current = 0
            while aux > 0:
                if aux % 10 in rotations:
                    current += rotations[aux % 10]*10**it
                    it += 1     
                else: break
                aux = aux // 10
            if aux == 0 and current != i:
                good = True
            if good: goods += 1
        
        return goods