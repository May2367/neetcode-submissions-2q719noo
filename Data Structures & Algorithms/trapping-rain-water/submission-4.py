class Solution:
    def trap(self, height: List[int]) -> int:
        #Prefix and Suffix

        h = len(height)
        left_max = [0] * h
        right_max = [0] * h
        
        for i in range(1, h):
            left_max[i] = max(left_max[i - 1], height[i - 1])
            right_max[h - 1 - i] = max(right_max[h - i], height[h - i])

        water_area = 0
        for i in range(1, h - 1):
            curr_water = min(left_max[i], right_max[i]) - height[i]
            if curr_water > 0:
                water_area += curr_water

        return water_area