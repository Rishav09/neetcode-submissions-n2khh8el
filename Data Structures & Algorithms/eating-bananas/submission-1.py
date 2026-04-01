import math
class Solution:
    def minEatingSpeed(self,piles, h):
        def canEatInTime(k):
            hours = 0
            for pile in piles:
            # Calculate how many hours it takes to eat this pile at speed k
                hours += math.ceil(pile/k)  # Equivalent to math.ceil(pile / k)
            return hours <= h
    
        left, right = 1, max(piles)  # Speed range: from 1 to max pile size
        while left < right:
            mid = left + (right - left) // 2  # Middle speed
            if canEatInTime(mid):
                right = mid  # Try smaller speeds
            else:
                left = mid + 1  # Try larger speeds
    
        return left  # The minimum speed that works
