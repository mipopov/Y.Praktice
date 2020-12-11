def DFS(n, graph, start_v):
    visited = [False] * (n + 1)
    res = []
    go = [start_v]

    while go:
        u = go.pop()
        if not visited[u]:
            visited[u] = True
            res.append(u)
            go.extend(sorted(graph[u], reverse=True))
    return res


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        if u == v:
            graph[u].append(v)
        else:
            graph[u].append(v)
            graph[v].append(u)
    start_v = int(input())
    if m == 0:
        print(start_v)
    else:
        print(*DFS(n, graph, start_v))