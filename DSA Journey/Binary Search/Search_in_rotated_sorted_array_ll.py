class Solution:
    def searchInARotatedSortedArrayII(self, nums, k):
        low = 0
        high =  len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid]==k:
                return True
            if nums[low] == nums[mid] == nums[high]:
                low = low + 1
                high = high - 1
                continue 
            elif nums[low]<=nums[mid]:
                if nums[low]<=k<nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            elif nums[high]>=nums[mid]:
                if nums[high]>=k>nums[mid]:
                    low = mid+1
                else:
                    high = mid-1
        return False