class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        nums.sort()
        curr = nums[0]
        index = 0
        while index != len(nums) - 1:
            if curr == nums[index + 1]:
                return True
            else:
                curr = nums[index + 1]
                index += 1
        return False