class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
            
        fib1, fib2 = 1, 1

        for i in range(2, n):
            temp = fib2
            fib2 += fib1
            fib1 = temp

        return fib1 + fib2