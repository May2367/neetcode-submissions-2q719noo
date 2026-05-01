class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums = sorted(nums)

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            target = 0 - nums[i]

            while(l < r):
                if nums[l] + nums[r] == target:
                    triplets.add(tuple(sorted((nums[l], nums[r], nums[i]))))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1

        return [list(t) for t in triplets]