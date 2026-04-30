class Solution:

    def encode(self, strs: List[str]) -> str:
        secured = ""
        for string in strs:
            length = len(string)
            secured += str(length) + "#" + string

        return secured

    def decode(self, s: str) -> List[str]:
        strs = []

        i = 0
        word_counter = -1
        while i < len(s):
            length = ""
            curr_char = s[i]
            while curr_char != "#":
                length += curr_char
                i += 1
                curr_char = s[i]

            if length == 0:
                strs[len(strs) + word_counter:] = [""]

                word_counter += 1
                i = i + 2
            else:
                string = ""
                for j in range(1, int(length) + 1):
                    string += s[i + j]
                
                strs[len(strs) + word_counter:] = [string]
                word_counter += 1

                i = i + int(length) + 1

        return strs