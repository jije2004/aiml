def dfs(graph, start, visited=None):
 if visited is None:
 visited = set()
 visited.add(start)
 print(start, end=" ")
 for neighbor in graph[start]:
 if neighbor not in visited:
 dfs(graph, neighbor, visited)
# Example graph as an adjacency list
graph = {
 '5' : ['3','7'],
'3' : ['2', '4'],
'7' : ['8'],
'2' : [],
'4' : ['8'],
'8' : []
}
# Start DFS from '5'
dfs(graph, '5')
