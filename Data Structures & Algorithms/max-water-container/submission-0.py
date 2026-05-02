class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Brute Force: max variable to track maximum amount of water
        #as we iterate through the array. Then we will use nested for loops
        #to try all possible combinations.

        max_container = -1

        for i in range(len(heights) - 1):
            for j in range(i + 1, len(heights)):
                if heights[i] < heights[j]:
                    curr_max = heights[i] * (j - i)
                else:
                    curr_max = heights[j] * (j - i)

                if curr_max  > max_container:
                    max_container = curr_max

        return max_container

        #heights = [0, 0]