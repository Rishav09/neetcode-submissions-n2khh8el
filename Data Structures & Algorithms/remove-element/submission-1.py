# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         temp = []
#         for i in range(len(nums)):
#             if nums[i]!=val:
#                 temp.append(nums[i])
#         for i in range(len(temp)):
#             nums[i] = temp[i]
#         return len(temp)
        
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]= nums[i]
                k+=1
        return k