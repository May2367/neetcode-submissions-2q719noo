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

# Let T = total tasks, K = unique task types, n = cooldown

# Time: O(T(n+1)log K)
# Space: O(K+n)

# Frequency counting: O(T)
# Heap construction: O(K log K)
# Queue initialization: O(n)

# Worst-case number of CPU cycles occurs when tasks
# are either all unique or all identical:

# T + (T-1)*n -> O(Tn), when n > 0

# Each cycle can perform heap operations costing O(log K).
# Therefore, total time is O(Tnlog K).
