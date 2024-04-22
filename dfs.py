import collections 
def dfs (graph, start, visited=None):
    if visited is None:
        visited=set()
    visited.add(start)
    print(start, end="")
    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)
if __name__ == '__main__' :
    graph={'A': ['B','C'], 'B':['D','E'], 'C':['F'], 'D':[], 'E':['F'], 'F':[] }
    print("DFS traversal starting from node 'A': ")
    dfs(graph, 'A')
