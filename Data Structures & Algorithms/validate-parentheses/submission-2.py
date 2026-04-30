class Solution:
    def isValid(self, s: str) -> bool:
        pairs= {')':'(','}':'{',']':'['}
        p_stack = []
        for i in s:
            if i in '({[':
                p_stack.append(i)
            elif not p_stack or pairs[i]!=p_stack.pop():
                return False
        return not p_stack