class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        left = 0
        n = len(s)

        spaceCount = 0

        for right in range(n):
            # space encountered
            if s[right] == " ":
                spaceCount += 1
            
            # word encountered after space
            # jump left to right and make space count 0
            if spaceCount != 0 and s[right] != " ":
                left = right
                spaceCount = 0
        
        # if last spaces remains then deduct the right about spaceCount
        if spaceCount:
            right = right - spaceCount
            

        print(s[left:right+1])

        return right - left + 1