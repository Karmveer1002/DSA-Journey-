class Solution:
    def insertionSort(self, nums):

        def sort(n):
            if n <= 1:
                return

            sort(n - 1)

            key = nums[n - 1]
            j = n - 2

            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]
                j = j - 1

            nums[j + 1] = key

        sort(len(nums))
        return nums