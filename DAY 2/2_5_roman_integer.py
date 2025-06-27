class Solution:
    def romanToInt(self, s: str) -> int:
        char_map = {
            'I': [0, 1],
            'V': [1, 5],
            'X': [2, 10],
            'L': [3, 50],
            'C': [4, 100],
            'D': [5, 500],
            'M': [6, 1000]
        }
        
        c = 0
        num = 0
        
        while c < len(s):
            char = s[c]
        
            if c == len(s) - 1:
                num += char_map[char][1]
            else:
                next_char = s[c+1]
                if char_map[char][0] < char_map[next_char][0]:
                    num += (char_map[next_char][1] - char_map[char][1])
                    c += 1
                else:
                    num += char_map[char][1]
            
            c += 1
        
        return num