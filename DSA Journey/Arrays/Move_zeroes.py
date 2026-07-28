class Solution:
    def moveZeroes(self, nums):
        for i in range(len(nums)):
            if nums[i] == 0:
                temp = nums[i]
                for j in range(i+1,len(nums)):
                    if nums[j]!=0:
                        nums[i]=nums[j]
                        nums[j] = temp 
                        break
                    
        return nums
