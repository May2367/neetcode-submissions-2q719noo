class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        left = 0
        right = len(s) - 1

        while left < right:
            l = s[left]
            r = s[right]

            while left < right and not('a' <= l <= 'z' or '0' <= l <= '9'):
                left += 1
                l = s[left]

            while left < right and not('a' <= r <= 'z' or '0' <= r <= '9'):
                right -= 1
                r = s[right]

            if l != r:
                print(l, r)
                return False
            else:
                left += 1
                right -= 1

        return True