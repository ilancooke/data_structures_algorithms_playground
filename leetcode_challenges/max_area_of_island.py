'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 50
    grid[i][j] is either 0 or 1.

    
My thoughts:
this is going to be the same algorithm as number of islands, but instead of counting the number of islands, we will count the area of each island and keep track of the max area seen so far


'''


def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
	m = len(grid) # number of rows
	n = len(grid[0]) # number of columns
	islands = []
	visited = set()
	for row in range(m):
		for column in range(n):
			if grid[row][column] == 1 and (row,column) not in visited:
				island = []
				queue = deque([(row,column)])
				
				while queue:
					node = queue.popleft()
					r, c = node
					#check for valid nodes
					if r<0 or r>=m or c<0 or c>=n or (r,c) in visited or grid[r][c] != 1:
						continue
					island.append(node)
					visited.add(node)
					#look for neighbors
					queue.append((r+1, c))
					queue.append((r-1, c))
					queue.append((r, c+1))
					queue.append((r, c-1))
					
				islands.append(island)
	if islands:
		return max(len(island) for island in islands)	
	else:
		return 0