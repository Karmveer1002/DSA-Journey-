class Solution:

    def bubbleSort(self, nums):
        self.sort(nums, len(nums))
        return nums

    def sort(self, nums, n):

        if n == 1:
            return

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

        self.sort(nums, n - 1)