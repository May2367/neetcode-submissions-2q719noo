class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = {}
        max_len = 0

        curr_start = 0
        for i, j in enumerate(s):
            if j in char_set:
                max_len = max(max_len, len(char_set))

                temp = char_set[j] + 1
                for k in range(char_set[j], curr_start - 1, -1):
                    char_set.pop(s[k])

                curr_start = temp
                char_set[j] = i
            else:
                char_set[j] = i

        max_len = max(max_len, len(char_set))

        return max_len