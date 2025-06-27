def prime(n):
    if n <= 1:
        return False
        
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        freq_map = dict()
        for i in nums:
            if i not in freq_map:
                freq_map[i] = 1
            else:
                freq_map[i] += 1
                    
        print(freq_map)

        p = [prime(freq) for num, freq in freq_map.items()]

        return True in p