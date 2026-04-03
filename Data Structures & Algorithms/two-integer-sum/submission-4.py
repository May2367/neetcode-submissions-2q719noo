class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = dict()

        #index = 0
        for i, n in enumerate(nums):
            if n in hash_table:
                return [hash_table[n], i]
            else:
                hash_table[target - n] = i
            
            #index += 1