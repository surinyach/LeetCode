class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        types = 0
        added = set()
        candies = len(candyType) / 2
        
        for c in candyType:
            if c not in added:
                types += 1
                added.add(c)
                if types == candies:
                    break
        
        return types