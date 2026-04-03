class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = dict()

        for string in strs:
            char_arr = [0] * 26
            for char in string:
                char_arr[ord(char) - ord('a')] += 1
            
            char_arr = tuple(char_arr)
            if char_arr in word_map:
                word_map[char_arr].append(string)
            else:
                word_map[char_arr] = [string]

        return list(word_map.values())
