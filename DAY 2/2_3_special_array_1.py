class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # f = [(nums[i] % 2 == 0)^(nums[i+1] % 2 == 0) for i in range(len(nums) - 1)]
        # return False not in f

        for i in range(len(nums) - 1):
            if not (nums[i] % 2 == 0)^(nums[i+1] % 2 == 0):
                return False
        return True