class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        rows, cols = len(grid), len(grid[0])
        fresh = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    q.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        time = 0

        while q and fresh > 0:
            for i in range(len(q)):
                curr_x, curr_y = q.popleft()

                for dx, dy in directions:
                    nx, ny = curr_x + dx, curr_y + dy

                    if (0 <= nx < rows and
                        0 <= ny < cols and
                        grid[nx][ny] == 1):

                        grid[nx][ny] = 2
                        fresh -= 1
                        q.append((nx, ny))

            time += 1

        return time if fresh == 0 else -1