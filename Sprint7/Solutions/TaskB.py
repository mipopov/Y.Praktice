from collections import deque


def bfs(graph, start_vert):
    color = {}
    parent = {}

    for (vert, _) in graph.items():
        if vert != start_vert:
            color[vert] = "white"

    color[start_vert] = "grey"
    deq = deque([start_vert])
    while deq:
        u = deq.popleft()
        for v in sorted(list(graph[u])):
            if color[v] == "white":
                parent[v] = u
                deq.append(v)
                color[v] = "grey"
        color[u] = "black"

    return parent


if __name__ == "__main__":
    graph_size = input().split()
    n = graph_size[0]
    m = int(graph_size[1])
    graph = {}
    i = 0
    while i < m:
        inp_str = input().split()
        u = int(inp_str[0])
        v = int(inp_str[1])
        if u != v:
            if graph.get(u):
                graph[u].add(v)
            else:
                graph[u] = {v}

            if graph.get(v):
                graph[v].add(u)
            else:
                graph[v] = {u}
        i += 1

    start_vert = int(input())
    if n == "1":
        print(start_vert)
    else:
        print(start_vert, *bfs(graph, start_vert))
