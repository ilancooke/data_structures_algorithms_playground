'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

 

Constraints:

    1 <= numCourses <= 2000
    0 <= prerequisites.length <= 5000
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    All the pairs prerequisites[i] are unique.


My thoughts:
It seems like I first need to construct a directed graph.
I'm not sure what format this takes, perhaps an adjacency list I can loop thru with a BFS?
How to choose where to start traversal?
I'm not sure what numCourses is describing here. 
Is it the number of unique courses in the prerequisite array?
Is it the total allowable courses one can take?


'''
def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    processed_count = 0
    graph = defaultdict(list)
    indegree = {course: 0 for course in range(numCourses)}
    for element in prerequisites:
        course = element[0]
        prereq = element[1]
        graph[prereq].append(course)
        indegree[course] += 1
        
    queue = deque([course for course in indegree if indegree[course]==0])
    while queue:
        course = queue.popleft()
        processed_count += 1
        unlocked_courses = graph[course]
        for unlocked in unlocked_courses:
            indegree[unlocked] -= 1
            if indegree[unlocked] == 0:
                queue.append(unlocked)

    return processed_count == numCourses