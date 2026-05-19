'''
You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

    Begin with the starting pixel and change its color to color.
    Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
    Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
    The process stops when there are no more adjacent pixels of the original color to update.

Return the modified image after performing the flood fill.

 

Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

Output: [[2,2,2],[2,2,0],[2,0,1]]

Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0

Output: [[0,0,0],[0,0,0]]

Explanation:

The starting pixel is already colored with 0, which is the same as the target color. Therefore, no changes are made to the image.

'''

def flood_fill(image, sr, sc, color):
	n = len(image) # number of rows
	m = len(image[0]) # number of columns
	old_color = image[sr][sc]
	
	if old_color == color:
		return image
		
	queue = deque([(sr, sc)])
	while queue:
		i, j = queue.popleft()
		if i<0 or i>=n or j<0 or j>=m or image[i][j] != old_color:
			continue
		else:
			image[i][j] = color
			queue.append((i+1, j))
			queue.append((i-1, j))
			queue.append((i, j+1))
			queue.append((i, j-1))
	
	return image

'''
Pattern: Graph traversal / connected component traversal; can use either BFS or DFS; I opted for BFS here.
Why this pattern: The problem requires exploring all adjacent pixels that have the same color as the starting pixel, which is a classic BFS use case.
Key data structure: Queue (deque)
'''