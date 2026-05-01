class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()

        for num in nums:
            num_set.add(num)

        size = 0
        while num_set:
            num = num_set.pop()
            curr_size = 1

            cpy = num - 1
            while cpy in num_set:
                num_set.remove(cpy)
                cpy -= 1
                curr_size += 1

            cpy = num + 1
            while cpy in num_set:
                num_set.remove(cpy)
                curr_size += 1
                cpy += 1

            if curr_size > size:
                size = curr_size

        return size