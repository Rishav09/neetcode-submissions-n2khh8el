class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for element in strs[1:]:
            j = 0
            while j<len(prefix) and j<len(element)and prefix[j]==element[j]:
                j+=1
            prefix = prefix[:j]
            if prefix == "":
                break
        return prefix