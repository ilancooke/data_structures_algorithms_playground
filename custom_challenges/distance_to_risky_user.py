'''
Airbnb represents relationships between users as an undirected graph. Each user is a node, and each relationship between two users is an edge.

Some users have previously been ghosted for policy violations. Airbnb wants to understand how close a new user is to any previously ghosted user.

Given:

n: the number of users, labeled 0 to n - 1
edges: a list of undirected relationships between users
ghosted_users: a list of users who were previously ghosted
new_user: the user we want to evaluate

Return the minimum number of relationship hops between new_user and any ghosted user.

Constraints:
1 <= n <= 100,000
0 <= len(edges) <= 200,000
0 <= user_id < n
edges[i] = [a, b]
ghosted_users may contain one or more users
The graph may be disconnected
The graph may contain cycles

If the new user is not connected to any ghosted user, return -1.
Example 1:
Input: n = 6, edges = [[0,1],[0,2],[1,3],[2,3],[3,4],[4,5]], ghosted_users = [5], new_user = 0
Output: 3
Explanation: The path from user 0 to user 5 is 0 -> 2 -> 3 -> 4 -> 5, which has 3 relationship hops.




'''


from collections import deque, defaultdict

def distance_to_nearest_ghosted_user(n, edges, ghosted_users, new_user):
    #convert ghosted_users to a set for quicker lookups
    ghosted_users = set(ghosted_users)
    # create an adjacency list
    graph = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0]) # other waya round for undirected graph
    
    
    visited = set()
    queue = deque([(new_user, 0)])
    visited.add(new_user)
    while queue:
        node, distance = queue.popleft()
        if node in ghosted_users:
            return distance
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, distance+1))
                visited.add(neighbor)
    
    return -1
