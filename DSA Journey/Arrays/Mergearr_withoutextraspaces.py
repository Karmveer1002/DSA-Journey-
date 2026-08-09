class Solution:
    def merge(self, nums1, m, nums2, n):

        gap = (m + n + 1) // 2

        while gap > 0:
            left = 0
            right = gap

            while right < m + n:
             
                if right < m:
                    if nums1[left] > nums1[right]:
                        nums1[left], nums1[right] = nums1[right], nums1[left]

                elif left < m:
                    if nums1[left] > nums2[right - m]:
                        nums1[left], nums2[right - m] = nums2[right - m], nums1[left]

                else:
                    if nums2[left - m] > nums2[right - m]:
                        nums2[left - m], nums2[right - m] = nums2[right - m],nums2[left - m]

                left += 1
                right += 1

            if gap == 1:
                break
            gap = (gap + 1) // 2

        for i in range(n):
            nums1[m + i] = nums2[i]