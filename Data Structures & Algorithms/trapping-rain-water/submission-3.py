class Solution:
    def trap(self, height: List[int]) -> int:
        #Brute Force
        if len(height) < 3:
            return 0

        l, r = 0, 1
        water_area = 0

        while l < r:
            while height[l] <= height[r] and r < len(height) - 1:
                l += 1
                r = l + 1
            
            curr_sum = 0
            local_max = 0
            index = -1
            for i in range(r, len(height)):
                if height[i] > local_max or height[i] >= height[l]:
                    local_max = height[i]
                    index = i
                if local_max >= height[l]:
                    break
            
            if index != r:
                curr_min = min(local_max, height[l])
                for i in range(r, index):
                    curr_sum += curr_min - height[i]

            if curr_sum != 0:
                water_area += curr_sum
                l = index
                r = l + 1
            else:
                l += 1
                r = l + 1

            if r > len(height) - 1:
                break

        return water_area