class Solution:
    def findLHS(self, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        s_len = 0
        nums.sort()

        for right in range(n):
            while nums[right] - nums[left] > 1:
                left += 1
            if nums[left] == nums[right] + 1 or nums[left] + 1 == nums[right]:
                s_len = right - left + 1 if right - left + 1 > s_len else s_len

        return s_len