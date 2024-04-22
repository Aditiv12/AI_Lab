#Prim's working
G = [
    [0, 19, 5, 0, 0],
    [19, 0, 5, 9, 2],
    [5, 5, 0, 1, 6],
    [0, 9, 1, 0, 1],
    [0, 2, 6, 1, 0]
]
selected_node = [False] * len(G)

edge = 0
while edge < len(G) - 1:
    min_weight = float('inf')
    a = 0  # Edge's starting node
    b = 0  # Edge's ending node
    for m in range(len(G)):
        if selected_node[m]:
            for node in range(len(G)):
                if not selected_node[node] and G[m][node]:
                    if min_weight > G[m][node]:
                        min_weight = G[m][node]
                        a = m
                        b = node
    print(f"Selected edge: {a}-{b}, Weight: {G[a][b]}")
    selected_node[b] = True
    edge += 1
