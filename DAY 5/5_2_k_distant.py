class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        if len(set(nums)) == 1:
            return [i for i in range(len(nums))]
            
        key_loc = []

        n = len(nums)

        for i in range(n):
            if nums[i] == key:
                key_loc.append(i)

        ans = {}

        for i in key_loc:
            ans[i] = True
            for j in range(1, k+1):
                a = i - j
                b = i + j
                
                print(a,b)
                if a not in ans and a>=0:
                    ans[a] = True
                if b not in ans and b<n:
                    ans[b] = True

        return sorted(list(ans.keys()))