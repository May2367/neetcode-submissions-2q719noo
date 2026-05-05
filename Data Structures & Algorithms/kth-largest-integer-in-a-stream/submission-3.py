class KthLargest:

    # Simpler Version

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [i for i in nums]
        heapq.heapify(self.heap)

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]

    # Run Time: O(nlogn), O(logk), Space Complexity: O(k)