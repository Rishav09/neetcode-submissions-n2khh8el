class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        result = {}
        for num in nums:
            result[num] = result.get(num,0)+1

        for key, value in result.items():
            if value>1:
                return True
        return False
        