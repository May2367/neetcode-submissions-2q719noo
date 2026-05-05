class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost to get to some place n is the min between the cost to get
        # to get to n - 1 and n - 2 plus the cost to on each of those tiles

        n = len(cost)
        dp = [0] * n

        for i in range(2, n):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        
        print(dp)

        return min(dp[n - 1] + cost[n - 1], dp[n - 2] + cost[n - 2])