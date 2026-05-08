class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # Lambdas is a one-line function. parameters : action -> returns automatically
        # Is useful to pass functions as a parameter and short functions used once or more times
        intervals.sort(key= lambda int: int[0])
        count = 0

        for i in range(1, len(intervals)):
            curr = intervals[i]
            prev = intervals[count]

            # The interval overlaps with the previous one
            if prev[0] <= curr[0] and curr[0] <= prev[1]:
                intervals[count] = [prev[0], max(prev[1], curr[1])]
                
            # The interval do not overlap with the previous one
            else: 
                count += 1
                intervals[count] = curr
        
        return intervals[0:count + 1]
    
    # Time Complexity: O(nlogn) -> sort cost, where n is the number of intervals
    # Space Complexity: O(k) -> where k are the merged intervals, since the slice creates a new list