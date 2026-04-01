class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive = 0
        max_number = 0
        for i in range(len(nums)):
            if nums[i]==1:
                consecutive+=1
                if consecutive > max_number:
                    max_number = consecutive
            else:
                consecutive=0
        return max_number
