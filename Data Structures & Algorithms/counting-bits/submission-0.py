class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)
        for i in range(n + 1):
            curr_ttl = 0
            for j in range(10):
                curr_ttl += (i >> j) & 1
            
            output[i] = curr_ttl

        return output