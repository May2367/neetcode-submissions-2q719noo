class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sumOfSquares(n: int) -> int:
            output = 0
            while n != 0:
                output += (n % 10) ** 2
                n = n // 10
                
            return output
            
        slow, fast = n, sumOfSquares(n)

        while slow != fast:
            if fast == 1:
                return True
                
            slow = sumOfSquares(slow)
            fast = sumOfSquares(sumOfSquares(fast))

        return slow == 1