class Solution:
    def trap(self, height: List[int]) -> int:
        #Two Pointers

        l, r = 1, len(height) - 2
        left_max, right_max = height[0], height[r + 1]
        water_area = 0

        while l <= r:
            print(height[l], height[r])
            if left_max < right_max:
                curr_area = left_max - height[l]
                l += 1
                left_max = max(left_max, height[l - 1])
            else:
                curr_area = right_max - height[r]
                r -= 1
                right_max = max(right_max, height[r + 1])

            print(curr_area)
            if curr_area > 0:
                water_area += curr_area

        return water_area