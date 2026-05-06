class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1:
            return True
        elif not s2:
            return False
        
        count_1 = Counter(s1)
        length = len(s1)
        if length > len(s2):
            return False

        for i in range(len(s2)):
            if s2[i] not in count_1:
                continue
            else:
                count_2 = Counter(s2[i:i + length])
                if count_1 == count_2:
                    return True

        return False