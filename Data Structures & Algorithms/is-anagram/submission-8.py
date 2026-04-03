class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_table = [0] * 26
        for char in s:
            hash_table[ord(char) - ord('a')] += 1
        
        for char in t:
            if(hash_table[ord(char) - ord('a')] == 0):
                return False
            else:
                hash_table[ord(char) - ord('a')] -= 1
        
        for i in hash_table:
            if i != 0:
                return False
        
        return True