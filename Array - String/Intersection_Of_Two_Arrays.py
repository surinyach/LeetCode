from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        sol = []
        i1, i2 = 0, 0
        while i1 < len(nums1) and i2 < len(nums2):
            n1 = nums1[i1]
            n2 = nums2[i2]
            if n1 == n2:
                sol.append(n1)
                while i1 < len(nums1) and nums1[i1] == n1:
                    i1 += 1
                while i2 < len(nums2) and nums2[i2] == n2:
                    i2 += 1
            elif n1 > n2:
                i2 += 1
            else:
                i1 += 1
        return sol