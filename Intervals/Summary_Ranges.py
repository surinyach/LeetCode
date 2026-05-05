class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        ranges = []
        interv = [nums[0], float(inf)]
        for i in range(1, len(nums)):
            n = nums[i]
            prev = nums[i-1]
            if n != prev + 1:
                if interv[1] == float(inf):
                    ranges.append(str(interv[0]))
                else:
                    ranges.append(str(interv[0]) + "->" + str(interv[1]))
                interv[0] = n
                interv[1] = float(inf)
            else:
                interv[1] = n

        if interv[1] == float(inf):
                    ranges.append(str(interv[0]))
        else:
            ranges.append(str(interv[0]) + "->" + str(interv[1]))
        
        return ranges