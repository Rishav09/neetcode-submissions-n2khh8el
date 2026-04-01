class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}  # Mapping of closing to opening brackets

        for char in s:
            if char in bracket_map:  # It's a closing bracket
                top_element = stack.pop() if stack else '#'  # Pop stack or use placeholder if empty
                if bracket_map[char] != top_element:
                    return False  # Mismatched bracket
            else:
                stack.append(char)  # It's an opening bracket, push to stack

        return not stack  # Return True if stack is empty (all brackets matched)
