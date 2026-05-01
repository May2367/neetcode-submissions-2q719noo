class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()

        for num in nums:
            num_set.add(num)

        size = 0
        for num in num_set:
            if num - 1 in num_set:
                continue
            else:
                curr_size = 1
                while num + 1 in num_set:
                    curr_size += 1
                    num += 1

                if curr_size > size:
                    size = curr_size

        return size