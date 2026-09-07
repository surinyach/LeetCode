class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key= lambda x: x[0])
        overlapping_section = points[0]
        arrows = 1
        for start, end in points[1:]:
            if start <= overlapping_section[1]:
                overlapping_section[0] = max(start, overlapping_section[0])
                overlapping_section[1] = min(end, overlapping_section[1])
            else:
                overlapping_section = [start, end]
                arrows += 1

        return arrows
    
        # Time Complexity: O(n log n) -> sorting dominates
        # Space Complexity: O(1)