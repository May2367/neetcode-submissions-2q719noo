class Solution:
    def isHappy(self, n: int) -> bool:
        squares = set()

        temp = n
        curr_sum = 0
        while temp != 1:
            while temp != 0:
                curr_sum += (temp % 10) * (temp % 10)
                temp = temp // 10

            if curr_sum in squares:
                return False
            else:
                squares.add(curr_sum)
                temp = curr_sum
                curr_sum = 0

        return True