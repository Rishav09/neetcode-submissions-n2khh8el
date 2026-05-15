class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        left, res = 0,0
        for right in range(len(s)):
            while s[right] in sett:
                sett.remove(s[left])
                left+=1
            sett.add(s[right])
            res = max(res, right-left+1)
        return res