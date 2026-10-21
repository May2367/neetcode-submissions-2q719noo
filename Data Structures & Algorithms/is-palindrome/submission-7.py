class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1

        while l < r:
            if not ('a' <= s[l] <= 'z' or '0' <= s[l] <= '9'):
                l += 1
                continue
            elif not ('a' <= s[r] <= 'z' or '0' <= s[r] <= '9'):
                r -= 1
                continue
            elif s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True