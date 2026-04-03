class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        n = len(self.nums)
        prefix = [0]*n
        prefix[0] = self.nums[0]
        for i in range(1,n):
            prefix[i]=prefix[i-1]+self.nums[i]
        if left == 0:
            rangeSum = prefix[right]
        else:
            rangeSum = prefix[right] - prefix[left-1]
        return rangeSum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)