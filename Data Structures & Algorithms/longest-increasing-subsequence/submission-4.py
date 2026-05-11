class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Binary Search
        tails = []

        for num in nums:
            l, r = 0, len(tails)

            while l < r:
                m = (l + r) // 2
                if tails[m] < num:
                    l = m + 1
                else:
                    r = m

            if l == len(tails):
                tails.append(num)
            else:
                tails[l] = num

        return len(tails)

        # Run Time: O(nlogn), Space Complexity: O(n)