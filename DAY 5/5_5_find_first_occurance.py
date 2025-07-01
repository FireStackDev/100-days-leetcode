class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)

        print(h,n, h-n)

        for i in range(h-n+1):
            print(haystack[i:i+n])
            if haystack[i:i+n] == needle:
                return i
        
        return -1