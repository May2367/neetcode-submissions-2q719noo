class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost to get to some place n is the min between the cost to get
        # to get to n - 1 and n - 2 plus the cost to on each of those tiles

        n = len(cost)
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        
        return dp[n]