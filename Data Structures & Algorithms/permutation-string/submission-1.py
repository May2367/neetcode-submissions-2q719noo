class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Brute Force
        count_1 = Counter(s1)
        length = len(s1)

        for i in range(len(s2) - length + 1):
            count_2 = Counter(s2[i:i + length])
            if count_1 == count_2:
                return True

        return False

        # Run Time: O(n*len(s1)), Space Complexity: O(n)