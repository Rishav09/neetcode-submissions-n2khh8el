class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target_sum = threshold * k
        counter= 0
        running_sum = sum(arr[:k])
        if running_sum >= target_sum:
            counter += 1
        for R in range(k, len(arr)):
            running_sum+=arr[R]
            running_sum-=arr[R-k]
            if running_sum>=target_sum:
                counter+=1
        return counter