class Solution:
    def isPalindrome(self, s: str) -> bool:
        string_lower = []
        for i in s:
            if i.isalnum():
                string_lower.append(i.lower())
        i,j = 0,len(string_lower)-1
        while(i<j):
            if string_lower[i]==string_lower[j]:
                i+=1
                j-=1
            else:
                return False
        
        return True
