class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        charS= {}
        charT = {}
        for char in s:
            charS[char]=charS.get(char,0)+1
        for char in t:
            charT[char]=charT.get(char,0)+1
        if charS==charT:
            return True
        else:
            return False