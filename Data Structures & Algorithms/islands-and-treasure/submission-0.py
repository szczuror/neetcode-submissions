class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647

        queue = deque()

        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            currRow, currCol, dist = queue.popleft()
            dist += 1
            for first, second in dirs:
                nr, nc = currRow + first, currCol + second

                # 
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == INF:
                        grid[nr][nc] = dist
                        queue.append((nr, nc, dist))