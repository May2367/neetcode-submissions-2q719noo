class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        if length > len(s2):
            return False

        count_1 = Counter(s1)
        count_2 = Counter(s2[0:length])

        for i in range(len(s2) - length + 1):
            if count_1 == count_2:
                return True
            else:
                if i == len(s2) - length:
                    continue

                count_2[s2[i]] -= 1
                if count_2[s2[i]] == 0:
                    count_2.pop(s2[i])

                count_2[s2[i + length]] = 1 + count_2.get(s2[i + length], 0)

        return False

        # Run Time: O(n), Space Complexity: O(1)