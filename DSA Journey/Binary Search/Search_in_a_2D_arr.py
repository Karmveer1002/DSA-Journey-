class Solution:
    def searchMatrix(self, mat, target):
        rows = len(mat)
        cols = len(mat[0])

        low = 0
        high = rows * cols - 1

        while low <= high:
            mid = (low + high) // 2

            row = mid // cols
            col = mid % cols

            if mat[row][col] == target:
                return True
            elif mat[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False