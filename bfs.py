from collections import deque
def bfs(graph, start):
 visited = set()
 queue = deque([start])
 while queue:
 vertex = queue.popleft()
 if vertex not in visited:
 print(vertex, end=" ")
 visited.add(vertex)
 queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)
# Example graph as an adjacency list
graph = {
'5' : ['3','7'],
'3' : ['2', '4'],
'7' : ['8'],
'2' : [],
'4' : ['8'],
'8' : []
}
# Start BFS from '5'
bfs(graph, '5')
