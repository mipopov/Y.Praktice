import sys
sys.setrecursionlimit(200000)


def DFS(v, visited,res):
    visited[v] = True
    res.append(v)
    for u in graph[v]:
        if not visited[u]:
            DFS(u, visited, res)
    return res


def dfs_order(v, visited, stack):
    visited[v] = True
    for i in new_graph[v]:
        if not visited[i]:
            dfs_order(i, visited, stack)
    stack.append(v)


def get_SC():
    stack = []
    visited = [False] * (n + 1)
    for i in range(n + 1):
        if not visited[i]:
            dfs_order(i, visited, stack)

    visited = [False] * (n + 1)
    new_graph.clear()
    while stack:
        new_v = stack.pop()
        if not visited[new_v]:
            new_graph.append(DFS(new_v, visited, []))
    return new_graph


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    new_graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        new_graph[v].append(u)

    res = get_SC()
    res.pop()
    for elem in res:
        elem.sort()

    res.sort(key=lambda x: x[0])
    print(len(res))
    for elem in res:
        elem.sort()
        print(*elem)

