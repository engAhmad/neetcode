class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        islands = 0
        visited = set()

# Depth First Search function
        def dfs(r, c):
            if (r not in range(rows) or c not in range(cols) or grid[r][c] == "0" or (r, c) in visited):
                return
            visited.add((r, c))
            # [0,1] cell under, [0,-1] cell above ,[1,0] cell right, [-1,0] cell left
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r+dr, c+dc)

        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)
        return islands

