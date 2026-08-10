#Approach 1 

class Solution:
    def isSorted(self, nums):
        return nums == sorted(nums)


#Approach 2

class Solution:
    def isSorted(self, nums):
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                return False
        return True 