class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        
        for task in tasks:
            if task in freq:
                freq[task] += 1
            else:
                freq[task] = 1

        heap = []

        for k, v in freq.items():
            heapq.heappush(heap, (-v, k))

        q = collections.deque([None] * (n + 1))
        cycles = 0
        remaining = len(tasks)

        while remaining > 0:
            expired = q.popleft()

            if expired is not None:
                heapq.heappush(heap, expired)

            if heap:
                curr_task = heapq.heappop(heap)
                curr_task = (curr_task[0] + 1, curr_task[1])
                remaining -= 1

                if curr_task[0] < 0:
                    q.append(curr_task)
                else:
                    q.append(None)
            else:
                q.append(None)
                
            cycles += 1

        return cycles
