class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = "abcdefghijklmnopqrstuvwxyz1234567890"
        n = len(s)
        clear_s = ""

        for i in range(n):
            char = s[i].lower()

            if char in valid:
                clear_s += char
        
        print(clear_s)
        m = len(clear_s)

        for i in range(m):
            if clear_s[i] != clear_s[(-1)*(i + 1)]:
                return False
        
        return True