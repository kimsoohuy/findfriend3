# graph.py
from collections import defaultdict

class Graph:
    def __init__(self):
        # mỗi key là node, value là set các neighbor
        self.adj = defaultdict(set)
    def has_node(self, u):
        # kiểm tra xem u có xuất hiện trong adjacency list chưa
        return u in self.adj
    def add_edge(self, u, v):
        self.adj[u].add(v)
        self.adj[v].add(u)

    def remove_edge(self, u, v):
        # discard() sẽ xoá nếu có, và im lặng nếu không có
        self.adj[u].discard(v)
        self.adj[v].discard(u)

    def neighbors(self, u):
        return list(self.adj.get(u, []))
    