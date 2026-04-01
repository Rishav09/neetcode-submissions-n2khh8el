class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_map = {}
        if not nums:
            return False
        for num in nums:
            my_map[num]=my_map.get(num,0)+1
        if max(my_map.values())>1:
            return True
        else:
            return False
         