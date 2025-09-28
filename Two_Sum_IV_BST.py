# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getNumbers(self, root, nums):
        if not root:
            return
        else:
            nums.append(root.val)
            self.getNumbers(root.left, nums)
            self.getNumbers(root.right, nums)
            return

    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        nums = []
        self.getNumbers(root, nums)

        for i in range(0, len(nums) - 1):
            current = nums[i]
            for j in range(i + 1, len(nums)):
                if current + nums[j] == k:
                    return True
        
        return False