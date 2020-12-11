import sys
sys.setrecursionlimit(200000)

global time
def DFS_vert(u):
    global time
    inp_time[u] = time
    time += 1
    vis[u] = 1

    for v in sorted(graph[u]):
        if vis[v] == 0:
            DFS_vert(v)

    out_time[u] = time
    time += 1


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    vis = [0] * (n + 1)
    inp_time = [0] * (n + 1)
    out_time = [0] * (n + 1)
    time = 0
    DFS_vert(1)
    for i in range(1, n + 1):
        print(inp_time[i], out_time[i])