class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rotten = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    rotten.add((row, col))

        time = 0

        while rotten:
            next_rotten = set()

            for x, y in rotten:
                res = 0

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy

                    if (0 <= nx < rows and
                        0 <= ny < cols and
                        grid[nx][ny] == 1):

                        grid[nx][ny] = 2
                        next_rotten.add((nx, ny))
                        res = 1

            if not next_rotten:
                break

            rotten = next_rotten
            time += 1

        for row in grid:
            if 1 in row:
                return -1

        return time
        