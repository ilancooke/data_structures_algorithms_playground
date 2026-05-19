'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.


    My thoughts:
    this is a connected components problem, I think I will solve with BFS
I will record islands as a list of lists where each list is a list of tuple coordinate pairs
loop through the entire grid
if cell value is 1:
check if it was already visited
visited will be a set of coordinate pair tuples
if not visited:
create new island as an empty list
add it to the BFS queue
while queue is not empty:
	node = popleft from the queue
	mark node as visited
	add node to island
	find neighbors up down left right, with appropriate guardrails for the grid edges and already seen cells
	add neighbors to the queue
	
when while loop finishes, you have an island and add it to islands list
return islands list length

    
    
    '''


def numIslands(self, grid: List[List[str]]) -> int:
	m = len(grid) # number of rows
	n = len(grid[0]) # number of columns
	islands = []
	visited = set()
	for row in range(m):
		for column in range(n):
			if grid[row][column] == '1' and (row,column) not in visited:
				island = []
				queue = deque([(row,column)])
				
				while queue:
					node = queue.popleft()
					r, c = node
					#check for valid nodes
					if r<0 or r>=m or c<0 or c>=n or (r,c) in visited or grid[r][c] != '1':
						continue
					island.append(node)
					visited.add(node)
					#look for neighbors
					queue.append((r+1, c))
					queue.append((r-1, c))
					queue.append((r, c+1))
					queue.append((r, c-1))
					
				islands.append(island)
	return len(islands)		