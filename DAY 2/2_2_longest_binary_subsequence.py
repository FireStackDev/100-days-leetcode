class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        kept = 0
        val = 0
        bits_used = 0

        for char in reversed(s):
            if char is "0":
                bits_used += 1
                kept += 1

            else:
                # if 1 increases the value then check if the value is less than k
                if val + (1 << bits_used) <= k:
                    val += (1 << bits_used)
                    bits_used += 1
                    kept += 1

            print(f"{char} => {val} ; {bits_used} ; {kept}")
        
        return kept