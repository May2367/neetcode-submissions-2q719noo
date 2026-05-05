class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [-i for i in nums]
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)

        temp = []
        for i in range(self.k):
            if self.heap:
                temp.append(heapq.heappop(self.heap))

        res = -temp[-1]

        for j in range(len(temp)):
            heapq.heappush(self.heap, temp[j])

        return res