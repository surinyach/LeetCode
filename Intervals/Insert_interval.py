class Solution(object):
    def insert(self, intervals, newInterval):
        """
        
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]

        intervals.append(newInterval)
        intervals.sort(key= lambda i: i[0])

        output = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= output[-1][1]:
                output[-1][1] = max(output[-1][1], end)
            else:
                output.append([start,end])

        return output

        # Time complexity = O(n log n) -> Where n is the number of intervals
        # Space complexity = O(k) -> Where k is the number of intervals after merging