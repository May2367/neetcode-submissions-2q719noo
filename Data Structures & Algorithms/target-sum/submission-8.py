class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # further optimized for space complexity

        dp = {}
        dp[0] = 1

        for num in nums:
            next_dp = {}

            for total, count in dp.items():
                if total + num in next_dp:
                    next_dp[total + num] += count
                else:
                    next_dp[total + num] = count
                
                if total - num in next_dp:
                    next_dp[total - num] += count
                else:
                    next_dp[total - num] = count

            dp = next_dp

        if target in dp:
            return dp[target]
        else:
            return 0
            