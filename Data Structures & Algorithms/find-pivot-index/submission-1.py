class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            leftSum=RightSum=0
            for j in range(i):
                leftSum+=nums[j]
            for k in range(i+1,n):
                RightSum+=nums[k]
            if leftSum == RightSum:
                return i
        return -1
