class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
            My initial thoughts lean towards sorting the list. Actually,
            maybe I could use a heap to keep track of element frequency. 
            Hash the list in O(n) using a dict, then convert the dict to 
            a heap and pop then return the top k elements. As a note, the 
            dict will be used more as a frequency table then a hash map.
        """

        freq_table = dict()

        for i in nums:
            if i in freq_table:
                freq_table[i] += 1
            else:
                freq_table[i] = 1
        
        min_heap = [(b, a) for a, b in list(freq_table.items())]
        heapq.heapify(min_heap)

        sol = []
        for j in range(0, len(min_heap) - k):
            heapq.heappop(min_heap)
        
        for i in range(0, k):
            sol.append(heapq.heappop(min_heap)[1])

        return sol