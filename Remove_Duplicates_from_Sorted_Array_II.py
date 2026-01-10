class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cont = 1
        k = 1
        ant = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            if num != ant or (num == ant and cont < 2):
                nums[k] = num
                k += 1
            
            if num == ant:
                cont += 1
            else:
                ant = num
                cont = 1
        return k