class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)

            if x == y:
                continue
            elif y < x:
                heapq.heappush(stones, -(x - y))

        if stones:
            return -stones[0]
        else:
            return 0

        # Run Time: O(nlogn), Space Complexity: O(n) 