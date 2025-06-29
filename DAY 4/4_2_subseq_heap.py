from heapq import nlargest
from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # 1) pair value with index
        paired = [(val, idx) for idx, val in enumerate(nums)]
        
        # 2) grab k largest by value (if values tie, nlargest keeps earlier idx first)
        top_k = nlargest(k, paired, key=lambda p: p[0])   # O(n log k)
        
        # 3) restore original order
        indices = sorted(idx for _, idx in top_k)         # O(k log k)
        return [nums[i] for i in indices]
