class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        smallest = 1
        largest = max(piles) + 1

        prev_rate = largest

        while smallest < largest:
            curr_rate = smallest + (largest - smallest) // 2

            time = 0
            for pile in piles:
                time += math.ceil(pile/curr_rate)

            if time <= h:
                prev_rate = curr_rate
                largest = curr_rate
            elif time > h:
                smallest = curr_rate + 1

        return prev_rate

        