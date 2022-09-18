class Solution:
    def isValid(self, s: str) -> bool:
        # Setting the stack as a list
        stack = []
        # Always keep the closing parenthesis first for mapping to the opening one
        closeToOpen = {")":"(","}":"{","]":"["}
        
        for c in s:
            # Check if c is closing parenthesis
            if c in closeToOpen:
                # stack[-1] is the last added element of the stack
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
