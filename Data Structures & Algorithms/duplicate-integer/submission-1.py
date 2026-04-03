class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """length = len(nums)
        index = 1
        for i in nums:
            for j in nums[index:length]:
                if i==j:
                    return True
            index += 1
        return False"

        "nums.sort()
        curr = nums[0]
        index = 0
        while curr != nums[len(nums) - 1]:
            if curr == nums[index + 1]:
                return True
            else:
                curr = nums[index + 1]
                index += 1
        return False"""

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
        