def DFS(n, graph, start_v, com_count):
    visited = [False] * (n + 1)
    stack = [start_v]

    while stack:
        u = stack.pop()
        if not visited[u]:
            visited[u] = True
            color_vertex[u] = com_count
            stack.extend(graph[u])

def find_components(n, graph):
    component_count = 1
    for v in range(n + 1):
        if color_vertex[v] == -1:
            DFS(n, graph, v, component_count)
        component_count += 1


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
    color_vertex = [-1] * (n + 1)
    find_components(n, graph)
    graph = {}
    for i in range(n + 1):
        if graph.get(color_vertex[i]):

            graph[color_vertex[i]].add(i)
        else:
            graph[color_vertex[i]] = {i}

    graph.pop(1)
    print(len(graph))
    for key in graph.values():
        print(*sorted(key))

