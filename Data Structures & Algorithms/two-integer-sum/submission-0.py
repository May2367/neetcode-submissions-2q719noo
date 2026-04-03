class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        hash_table = dict()

        index = 0;
        for i in nums:
            if i in hash_table:
                return [min(index, hash_table[i]), max(index, hash_table[i])]
            else:
                hash_table[target - i] = index
            
            index += 1