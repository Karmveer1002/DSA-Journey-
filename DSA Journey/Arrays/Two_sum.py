class Solution:
    def twoSum(self, nums, target):
        store={}
        for i in range (0,len(nums)):
            need = target - nums[i]
            if need in store:
                return [store[need],i]
            store[nums[i]] = i
        return[]