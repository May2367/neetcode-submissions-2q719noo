class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = {}
        max_len = 0

        curr_start = 0
        for i, j in enumerate(s):
            if j in char_set:
                max_len = max(max_len, i - curr_start)
                curr_start = max(curr_start, char_set[j] + 1)
                char_set[j] = i
            else:
                char_set[j] = i

        max_len = max(max_len, len(s) - curr_start)
        return max_len