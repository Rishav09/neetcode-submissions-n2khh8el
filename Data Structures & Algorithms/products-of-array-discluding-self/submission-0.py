class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        
        # Left products: product of all elements to the left of index i.
        left = 1
        for i in range(n):
            output[i] = left
            left *= nums[i]
        
        # Right products: product of all elements to the right of index i.
        right = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right
            right *= nums[i]
        
        return output