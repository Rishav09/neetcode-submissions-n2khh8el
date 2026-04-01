class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(','}':'{',']':'['}
        stack = []
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if not stack or stack.pop()!=pairs[i]:
                    return False
        return not stack
        