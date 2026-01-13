class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0
        max_pos = nums[0]
        prov_pos = nums[0]
        for i in range(1, len(nums)):
            prov_pos = max(prov_pos, nums[i] + i)
            if max_pos >= len(nums):
                jumps += 1
                break
            if i == max_pos:
                jumps += 1
                max_pos = prov_pos
        return jumps