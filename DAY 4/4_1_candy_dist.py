from math import comb

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        L = limit
        def choose2(x):       # returns C(x, 2) or 0 if x < 2
            return comb(x, 2) if x >= 2 else 0
        
        total = choose2(n + 2)

        # solutions where 1 getting extra + solutions where 2 getting extra + .... 
        minus1 = 3 * choose2(n - L - 1 + 2)

        # sol where 1 and 2 getting extra + sol where 2 and 3 getting extra + ....
        plus2 = 3 * choose2(n - 2*L - 2 + 2)

        # sol where all of them got extra
        minus3 = choose2(n - 3*L - 3 + 2)

        # first the sols where 1 child got extra is deducted
        # but the sols where 1 got extra also contains 2 child got extra which is deducted twice
        # so they are added
        # in the 2nd sols there was also 3 child got extra which is also added twice
        # so it was also deducted

        return total - minus1 + plus2 - minus3
