# 21 ноя 2020, 22:13:34 - ID - 42273394
import sys
from collections import defaultdict

sys.setrecursionlimit(200000)


class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.verts = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_cyclic_util(self, v, visited, rec_stack):
        visited[v] = True
        rec_stack[v] = True
        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                if self.is_cyclic_util(neighbour, visited, rec_stack):
                    return True
            elif rec_stack[neighbour]:
                return True
        rec_stack[v] = False
        return False

    def is_cyclic(self):
        visited = [False] * self.verts
        rec_stack = [False] * self.verts
        for node in range(self.verts):
            if not visited[node]:
                if self.is_cyclic_util(node, visited, rec_stack):
                    return True
        return False


if __name__ == "__main__":
    n = int(input())
    graph = Graph(n)
    for i in range(n - 1):
        line = input()
        count = i + 1
        for j in range(len(line)):
            if line[j] == 'R':
                graph.add_edge(count, i)
            else:
                graph.add_edge(i, count)
            count += 1
    if graph.is_cyclic() == 1:
        print("NO")
    else:
        print("YES")