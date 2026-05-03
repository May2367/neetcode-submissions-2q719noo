class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        for i in range(32):
            total += (n >> i) & 1

        return total