def DFS(n, graph, start_v):
    visited = [False] * (n + 1)
    go = [start_v]

    while go:
        u = go.pop()
        if not visited[u]:
            visited[u] = True
            go.extend(graph[u])
    if visited.count(True) == n:
        return True
    return False

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    new_graph = [[] for _ in range(n + 1)]
    u, v = 0, 0
    for _ in range(m):
        u, v = map(int, input().split())
        if u == v:
            graph[u].append(v)
        else:
            graph[u].append(v)
            new_graph[v].append(u)

    if DFS(n, graph, u) and DFS(n, graph, v):
        print("YES")
    else:
        print("NO")
