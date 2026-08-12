#Approach 1
class Solution:
    def unionArray(self, nums1, nums2):
        ans = []
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                if not ans or ans[-1] != nums1[i]:
                    ans.append(nums1[i])
                i += 1

            elif nums2[j] < nums1[i]:
                if not ans or ans[-1] != nums2[j]:
                    ans.append(nums2[j])
                j += 1

            else:
                if not ans or ans[-1] != nums1[i]:
                    ans.append(nums1[i])
                i += 1
                j += 1

        while i < len(nums1):
            if not ans or ans[-1] != nums1[i]:
                ans.append(nums1[i])
            i += 1

        while j < len(nums2):
            if not ans or ans[-1] != nums2[j]:
                ans.append(nums2[j])
            j += 1

        return ans

#Approach 2

class Solution:
    def unionArray(self, nums1, nums2):
        return sorted(set(nums1) | set(nums2))