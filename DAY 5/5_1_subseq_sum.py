class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        ans = 0

        while i <= j:
            if nums[i] + nums[j] <= target:
                ans = (ans + 2**(j - i)) % (10**9 + 7)
                i += 1
            else:
                j -= 1
        print(ans)
        return ans