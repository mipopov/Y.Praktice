
if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    weight = [[0] * (n + 1) for _ in range(n)]
    for i in range(m):
        u, v, w = map(int, input().split())
        graph[u].append(v)
        weight[u][v] = w
    print(weight)
