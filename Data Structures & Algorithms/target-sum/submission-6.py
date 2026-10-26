class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # This solution removes array slicing from the previous one
        # by tracking the index instead of the array
        
        dp = {}

        def recurse(i: int, curr_target) -> int:
            key = (i, curr_target)   

            if key in dp:
                return dp[key]

            if i < 0:
                return 1 if curr_target == 0 else 0
            else:
                temp = nums[i]
                dp[key] = (
                            recurse(i - 1, curr_target - temp)
                            + recurse(i - 1, curr_target + temp)
                          )
                return dp[key]

        return recurse(len(nums) - 1, target)
            