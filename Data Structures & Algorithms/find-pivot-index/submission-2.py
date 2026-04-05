class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        leftSum = 0
        for i, num in enumerate(nums):
            right_sum = total - leftSum - num
            if leftSum == right_sum:
                return i
            leftSum += num
        return -1
