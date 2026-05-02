class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #two pointer approach to maximize the distance between indices
        #left, right pointers at opposite sides
        #if incrementing left and decrementing right both decrease overall
        #area, which of the two should we move?
        #heights = [5,2,6,4,7,5,3,5]
        #

        max_size = -1
        l, r = 0, len(heights) - 1

        while l < r:
            curr_size = (r - l) * min(heights[l], heights[r])

            if curr_size > max_size:
                max_size = curr_size

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_size

        