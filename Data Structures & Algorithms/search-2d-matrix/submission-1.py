class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flattened_row = [val for row in matrix for val in row]

        n = len(flattened_row)
        left,right = 0, n-1
        while left<=right:
            mid = (left+right)//2
            if flattened_row[mid]==target:
                return True
            elif flattened_row[mid]>target:
                right = mid-1
            else:
                left = mid+1
            
        return False