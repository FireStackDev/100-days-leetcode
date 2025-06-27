class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        best = 0
        visited = dict()

        for i, item in enumerate(s):
            if item in visited and visited[item] >= left:
                # left window is updated to new one
                left = visited[item] + 1
            visited[item] = i # updated last seen

            best = max(best , i - left + 1)
        return best