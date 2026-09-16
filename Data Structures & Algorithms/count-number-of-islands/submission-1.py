class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # number of graph components
        # create a graph then do a bfs search

        # traverse through the matrix -> O(nm)
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        islands = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != "1" or (i, j) in visited:
                    continue
                visited.add((i, j))
                islands += 1

                stack = [(i, j)]
                while stack:
                    currRow, currCol = stack.pop()
                    for newRow, newCol in ((currRow - 1, currCol), (currRow + 1, currCol), (currRow, currCol - 1), (currRow, currCol + 1)):
                        if (
                            0 <= newRow < rows
                            and 0 <= newCol < cols
                            and grid[newRow][newCol] == "1"
                            and (newRow, newCol) not in visited
                        ):
                            visited.add((newRow, newCol))
                            stack.append((newRow, newCol))
        return islands