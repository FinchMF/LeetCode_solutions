import math

import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        seq, k, fact = "", k-1, math.factorial(n-1)
        perm = [i for i in range(1, n + 1)]
        
        for i in reversed(range(n)):
            
            curr = perm[int(k // fact)]
            seq += str(curr)
            perm.remove(curr)
            
            if i > 0:
                
                k %= fact
                fact /= i
                
        return seq


if __name__ == '__main__':

    print(Solution().getPermutation(n=4, k=2))
    print(Solution().getPermutation(n=4, k=3))
    print(Solution().getPermutation(n=4, k=4))
    print(Solution().getPermutation(n=4, k=5))
    print(Solution().getPermutation(n=4, k=6))

                   