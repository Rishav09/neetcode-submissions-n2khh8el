from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_works(k):
            hours = 0
            for one in piles:
                hours+=ceil(one/k)
            return hours<=h
        left, right = 1,max(piles)
        while left<right:
            k = (left+right)//2
            if k_works(k):
                right = k
            else:
                left = k+1
        return right