class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        rows, cols = len(grid), len(grid[0])

        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 1 or (r, c) in visited:
                    continue
                # else we do a dfs
                curr_area = 0
                stack = [(r, c)]
                visited.add((r,c))
                while stack:
                    currRow, currColumn = stack.pop()
                    curr_area += 1

                    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                    for dr, dc in dirs:
                        nr, nc = currRow + dr, currColumn + dc

                        if(rows > nr >= 0 and
                        cols > nc >= 0 and
                        (nr, nc) not in visited and
                        grid[nr][nc] == 1
                        ):
                            stack.append((nr, nc))
                            visited.add((nr, nc))
                max_area = max(max_area, curr_area)
        return max_area