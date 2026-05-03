class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        l, r = 0, 1
        water_area = 0

        while l < r:
            print("l, r: ", l, r)
            while height[l] <= height[r] and r < len(height) - 1:
                l += 1
                r = l + 1
            
            print("l, r after inner while 1: ", l, r)
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

            print("(curr_sum, l, r): ", curr_sum, l, r)#
            print("water_area: ", water_area)
            if curr_sum != 0:
                print("inside curr_sum != 0", curr_sum)
                water_area += curr_sum
                l = index
                r = l + 1
            else:
                l += 1
                r = l + 1

            if r > len(height) - 1:
                break

        return water_area