class Solution:
    def bubbleSort(self, nums):
        n = len(nums)

        for i in range(n):

            for j in range(n -1):

                if nums[j] > nums[j+1]:
                    nums[j+1], nums[j] = nums[j], nums[j+1]

        return nums