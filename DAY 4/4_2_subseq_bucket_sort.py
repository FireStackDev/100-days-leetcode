from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # 1. pair values with indices
        pairs = [(v, i) for i, v in enumerate(nums)]

        # 2. sort: primary = value (desc), secondary = index (asc)
        pairs.sort(key=lambda p: (-p[0], p[1]))      # O(n log n)

        # 3. keep the best k pairs
        top_k_idx = [idx for _, idx in pairs[:k]]

        # 4. restore original order of the subsequence
        top_k_idx.sort()                             # O(k log k)
        return [nums[i] for i in top_k_idx]
