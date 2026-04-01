class Solution:
    def hammingWeight(self, n: int) -> int:
        count_bits = 0
        while(n):
            if n&1:
                count_bits+=1
            n = n>>1
        return count_bits
        