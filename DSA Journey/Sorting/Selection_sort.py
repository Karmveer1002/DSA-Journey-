"Approach 1"

class Solution:
    def selectionSort(self, nums):
        
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[j] < nums[i]:                
                    nums[i], nums[j] = nums[j], nums[i]
        return nums
    
"Approach 2"

def selectionSort(arr):
    n = len(arr)

    for i in range(n - 1):
        minIndex = i

        for j in range(i + 1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j

        arr[i], arr[minIndex] = arr[minIndex], arr[i]

    return arr