def DFS(n, graph, start_v):
    visited[start_v] = True

    for i in graph[start_v]:
        if not visited[i]:
            DFS(n, graph, i)

    top_arr.append(start_v)


def top_sort(n, graph):
    for i in range(n + 1):
        visited[i] = False
    top_arr.clear()
    for i in range(n + 1):
        if not visited[i]:
            DFS(n, graph, i)

    return top_arr[:: -1][:-1]


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    u, v = 0, 0
    for _ in range(m):
        u, v = map(int, input().split())
        if u == v:
            graph[u].append(v)
        else:
            graph[u].append(v)
    visited = [False] * (n + 1)
    top_arr = []
    print(*top_sort(n, graph))
