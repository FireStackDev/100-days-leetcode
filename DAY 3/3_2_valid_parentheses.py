class Solution:
    def isValid(self, s: str) -> bool:
        close = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        stack = []

        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if not stack or close[stack.pop()] != i:
                    return False
        
        return True