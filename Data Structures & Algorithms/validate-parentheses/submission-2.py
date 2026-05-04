class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        print(s)
        
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if len(stack) == 0 or (s[i] == ')' and stack[-1] != '(') or (s[i] == ']' and stack[-1] != '[') or (s[i] == '}' and stack[-1] != '{'):
                    return False
                else:
                    stack.pop()

        if len(stack) != 0:
            return False
        else:
            return True