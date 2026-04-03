class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = dict()

        for i in nums:
            if i in freq_table:
                freq_table[i] += 1
            else:
                freq_table[i] = 1
        
        return [x[0] for x in heapq.nlargest(k, freq_table.items(), key=lambda x: x[1])]