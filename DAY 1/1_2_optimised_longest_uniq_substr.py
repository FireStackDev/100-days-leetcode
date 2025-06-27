class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = [-1] * 128      # fixed 128-slot table: ord(char) → last index
        left = best = 0
    
        for right, ch in enumerate(s):
            j = last[ord(ch)]
            if j >= left:      # duplicate inside current window
                left = j + 1   # jump left past it
            last[ord(ch)] = right
    
            # inlined max() (cheaper than calling the builtin each pass)
            cur_len = right - left + 1
            if cur_len > best:
                best = cur_len
    
        return best