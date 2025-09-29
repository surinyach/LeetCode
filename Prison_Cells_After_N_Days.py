class Solution(object):
    def prisonAfterNDays(self, cells, n):
        """
        :type cells: List[int]
        :type n: int
        :rtype: List[int]
        """
        seen = {}
        
        while n > 0:
            state = (tuple(cells))
            if state in seen: 
                cycle_length = seen[state] - n
                n %= cycle_length
            seen[state] = n
            
            if n > 0:
                n -= 1
                aux = [0]
                for j in range(1, len(cells) - 1):
                    aux.append(1) if cells[j - 1] == cells[j + 1] else aux.append(0)
                aux.append(0)
                cells = aux
                
        return cells