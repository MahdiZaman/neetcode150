class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closetoopen = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for c in s:
            if c in closetoopen:
                if stack and stack[-1] == closetoopen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if len(stack) == 0 else False
    
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()")) # True
    print(s.isValid("()[]{}"))  # True
    print(s.isValid("(]"))  # False
    print(s.isValid("([)]"))    # False
    print(s.isValid("{[]}"))    # True
    print(s.isValid("]"))   # False
    print(s.isValid("["))   # False