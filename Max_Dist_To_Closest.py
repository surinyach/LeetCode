class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        beg = -1
        fin = -1
        dist = 0
        max_dist = -1

        for i in range (0, len(seats)):
            s = seats[i]
            if s == 1:
                if beg == -1:
                    beg = dist
                else:
                    if dist > max_dist:
                        max_dist = dist
                dist = 0
            else: dist += 1
        
        fin = dist

        if beg > max_dist // 2 and beg > fin:
            return beg
        elif fin > max_dist // 2:
            return fin
        else:
            return max_dist // 2 if max_dist % 2 == 0 else max_dist // 2 + 1