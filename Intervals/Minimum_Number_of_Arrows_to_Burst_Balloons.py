class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key= lambda x: x[0])
        output = [points[0]]
        for start, end in points[1:]:
            if start <= output[-1][1]:
                output[-1][1] = min(output[-1][1], end)
            else:
                output.append([start, end])

        return len(output)
    
        # Time Complexity: O(n log n) -> sorting dominates
        # Space Complexity: O(n) -> output may store all intervals in the worst case