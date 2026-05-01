class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        left = 0
        right = len(s) - 1

        while left < right:
            l = s[left]
            r = s[right]

            if not('a' <= l <= 'z' or 'A' <= l <= 'Z' or '0' <= l <= '9'):
                left += 1
                continue

            if not('a' <= r <= 'z' or 'A' <= r <= 'Z' or '0' <= r <= '9'):
                right -= 1
                continue

            if l != r:
                return False
            else:
                left += 1
                right -= 1

        return True