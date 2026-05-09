class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        # 5 given coins = {1, 2, 3} is the number of ways you can make
        # number of ways you can make 4 given {1, 2, 3} + numWays toMake 3
        # given {2, 3} + num ways to make 2 given {3}. 
        # dp[5] = dp[4] + dp[3] + dp[2]
        # dp[n] = summation of dp[n - num] for num in coins
        # dp[0] = 1
        # dp[1] = for num in coins, if 0 + num = 1, then dp[1] += 1.
        # dp[2] = dp[2 - num1] + dp[2 - num2]... such that numi <= 2
        for num in coins:
            for i in range(1, len(dp)):
                if i - num >= 0:
                    dp[i] += dp[i - num]

        return dp[amount]