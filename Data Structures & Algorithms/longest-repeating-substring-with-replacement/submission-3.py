class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Two Pointer

        l, r = 0, 0
        hash_set = {}
        res = 0
        hash_set[s[l]] = 1
        while l != len(s) - 1:
            if (r - l + 1) - (max(hash_set.values())) <= k:
                if (r - l + 1) > res:
                    res = r - l + 1
            else:
                hash_set[s[l]] -= 1
                l += 1
                continue

            if r == len(s) - 1:
                hash_set[s[l]] -= 1
                l += 1
            else:
                r += 1
                if s[r] in hash_set:
                    hash_set[s[r]] += 1
                else:
                    hash_set[s[r]] = 1

        return res