class Solution:
    # def isPalindrome(self, s: str) -> bool:
    #     string_lower = []
    #     for i in s:
    #         if i.isalnum():
    #             string_lower.append(i.lower())
    #     i,j = 0,len(string_lower)-1
    #     while(i<j):
    #         if string_lower[i]==string_lower[j]:
    #             i+=1
    #             j-=1
    #         else:
    #             return False
        
    #     return True
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            # Skip non-alphanumeric characters from left
            while l < r and not s[l].isalnum():
                l += 1
            # Skip non-alphanumeric characters from right
            while l < r and not s[r].isalnum():
                r -= 1
            
            # Compare characters (case-insensitive)
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True