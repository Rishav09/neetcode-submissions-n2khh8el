class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        sett = {}
        for i in range(len(nums)):
            if nums[i] in sett and i-sett[nums[i]]<=k:
                return True
            sett[nums[i]]=i
        return False