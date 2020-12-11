from collections import deque


def bfs(graph, start_vert, end_vert):
    dist = {}
    color = {}

    for (vert, path) in graph.items():
        if vert != start_vert:
            color[vert] = "white"

    dist[start_vert] = 0
    color[start_vert] = "grey"
    deq = deque([start_vert])
    while deq:
        u = deq.popleft()
        if u == end_vert:
            return dist[u]
        if u not in graph:
            return -1
        for v in graph[u]:
            if color[v] == "white":
                if v == end_vert:
                    return dist[u] + 1
                else:
                    dist[v] = dist[u] + 1
                    deq.append(v)
                    color[v] = "grey"
        color[u] = "black"
    return -1


if __name__ == "__main__":
    graph_size = input().split()
    n = graph_size[0]
    m = int(graph_size[1])
    graph = {}
    i = 0
    while i < m:
        inp_str = input().split()
        u = inp_str[0]
        v = inp_str[1]
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

    input_str = input().split()
    start_v = input_str[0]
    end_v = input_str[1]
    print(bfs(graph, start_v, end_v))