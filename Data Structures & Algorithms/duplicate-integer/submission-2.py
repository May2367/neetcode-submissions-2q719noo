class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        index = 1
        for i in nums:
            for j in nums[index:length]:
                if i==j:
                    return True
            index += 1
        return False