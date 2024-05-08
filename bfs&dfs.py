#bfs dfs
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print("Visited node:", start)
        for neighbour in self.graph[start]:
            if neighbour not in visited:
                self.dfs(neighbour, visited)

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            node = queue.pop(0)
            print("Visited node:", node)
            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)

if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('B', 'E')
    graph.add_edge('C', 'F')
    graph.add_edge('E', 'F')

    print("DFS traversal starting from node 'A':")
    graph.dfs('A')

    print("\nBFS traversal starting from node 'A':")
    graph.bfs('A')
