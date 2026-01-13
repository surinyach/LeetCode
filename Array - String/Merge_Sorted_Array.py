class Solution(object):
    def merge(self, nums1, m, nums2, n):
       pn1 = m - 1 # Last element in nums1's initial part
       pn2 = n - 1 # # Last element in nums2
       pf = m + n - 1 # Last index of nums1

       # Merge in reverse order
       while pn2 >= 0:
            if pn1 >= 0 and nums1[pn1] > nums2[pn2]:
                nums1[pf] = nums1[pn1] 
                pn1 -= 1
            else:
                nums1[pf] = nums2[pn2]
                pn2 -= 1
            pf -= 1