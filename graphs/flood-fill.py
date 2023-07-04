class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        curr = image[sr][sc]
        rows = len(image)
        columns = len(image[0])

        def helper(r, c, grid):
            if r >= rows or r < 0 or c < 0 or c >= columns:
               return
            
            if grid[r][c] != curr or grid[r][c] == color:
                return
            grid[r][c] = color
            
            helper(r-1, c, grid)
            helper(r+1, c, grid)
            helper(r, c-1, grid)
            helper(r, c+1, grid)

        helper(sr, sc, image)
        return image
