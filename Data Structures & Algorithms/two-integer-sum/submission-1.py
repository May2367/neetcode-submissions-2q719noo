class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        hash_table = dict()

        index = 0
        for i in nums:
            if i in hash_table:
                return [hash_table[i], index]
            else:
                hash_table[target - i] = index
            
            index += 1