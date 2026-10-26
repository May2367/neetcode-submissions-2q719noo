class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def recurse(arr: List[int], curr_target) -> int:
            key = (tuple(arr), curr_target)

            if key in dp:
                return dp[key]

            if len(arr) == 0:
                return 1 if curr_target == 0 else 0
            else:
                temp = arr[-1]
                dp[key] = (
                            recurse(arr[:-1], curr_target - temp)
                            + recurse(arr[:-1], curr_target + temp)
                          )
                return dp[key]

        return recurse(nums, target)

"""
This is the brute force solution. Too slow for neetcode.

        def recurse(arr: List[int], target) -> int:
            if len(arr) == 0:
                return 1 if target == 0 else 0
            else:
                temp = arr[-1]
                return (recurse(arr[:-1], target - temp)
                        + recurse(arr[:-1], target + temp))

        return recurse(nums, target)
"""