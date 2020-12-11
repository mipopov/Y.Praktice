# 21 ноя 2020, 22:04:13 - ID - 42272889
import sys
sys.setrecursionlimit(200000)


KEY_PHRASE = "Oops! I did it again"


class Graph:
    def __init__(self, vertices):
        self.verts = vertices
        self.graph = []

    def add_edge(self, u, v, weight):
        self.graph.append([u, v, weight])

    def search(self, parent, i):
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.search(parent, x)
        y_root = self.search(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def Kruskal_MST(self):
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2], reverse=True)
        parent = []
        rank = []

        for node in range(self.verts):
            parent.append(node)
            rank.append(0)

        while self.verts - 1 > e:
            if i >= len(self.graph):
                return KEY_PHRASE
            u, v, w = self.graph[i]
            i = i + 1
            x = self.search(parent, u)
            y = self.search(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        minimumCost = 0
        for u, v, weight in result:
            minimumCost += weight
        return minimumCost


if __name__ == "__main__":
    n, m = map(int, input().split())
    if n == 1 and m == 0:
        print(0)
    elif n == 0 or m == 0:
        print(KEY_PHRASE)
    else:
        graph = Graph(n)
        for i in range(m):
            u, v, w = map(int, input().split())
            graph.add_edge(u - 1, v - 1, w)
        print(graph.Kruskal_MST())