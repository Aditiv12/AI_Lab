def bfs (graph, root):
    visited, queue=set(), collections.deque([root])
    visited.add(root)
    while queue:
        vertex = queue.popleft()
        print(str(vertex) +"", end="")
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
if __name__ == '__main__':
    graph={'A': ['B','C'], 'B':['D','E'], 'C':['F'], 'D':[], 'E':['F'], 'F':[] }
    print('BFS traversal starting from node A: ')
    bfs(graph, 'A')
