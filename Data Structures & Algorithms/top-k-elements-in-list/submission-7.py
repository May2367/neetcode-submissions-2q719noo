class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort

        hash_map = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            hash_map[n] = 1 + hash_map.get(n, 0)
        
        for m in hash_map:
            freq[hash_map[m]].append(m)

        res = []
        for i in range(len(nums), 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res