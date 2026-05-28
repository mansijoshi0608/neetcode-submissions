class Solution:
    def isValid(self, s1: str) -> bool:
        stack=[]
        for s in s1:
            if s == '[' or s=='{' or s=='(':
                stack.append(s)
            else:
                if stack and s=='}' and stack[-1]=='{':
                    stack.pop()
                elif stack and s==']' and stack[-1]=='[':
                    stack.pop()
                elif stack and s==')' and stack[-1]=='(':
                    stack.pop()
                else:
                    return False
        if len(stack)==0:
            return True
        return False
        