class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        boool = False
        for i in range(len(digits) - 1, -1, -1):
            if boool == True:
                break

            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                boool = True

        if boool == False:
            return [1] + digits
        else:
            return digits

        # Run Time: O(n), Space Complexity: O(1)