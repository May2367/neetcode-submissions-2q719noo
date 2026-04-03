class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        hash_table = [None] * length
        for i in range(0, length):
            idx = nums[i] % length
            if hash_table[idx] != None:
                if nums[i] == hash_table[idx]:
                   return True
                else:
                    curr = (idx + 1) % length
                    while hash_table[curr % length] != None:
                        if nums[i] == hash_table[curr]:
                            return True
                        else:
                            curr += 1
                        if curr >= idx + length:
                            break
                    if hash_table[curr % length] == None:
                        hash_table[curr % length] = nums[i]
            else:
                hash_table[idx] = nums[i]
        return False
        