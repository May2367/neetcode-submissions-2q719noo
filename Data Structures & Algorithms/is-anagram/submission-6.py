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

        """
        if len(s) != len(t):
            return False
        
        hash_table = [0] * 26
        for char_s, char_t in zip(s, t):
            hash_table[ord(char_s) - ord('a')] += 1
            hash_table[ord(char_t) - ord('a')] -= 1

        return not any(hash_table)
        """