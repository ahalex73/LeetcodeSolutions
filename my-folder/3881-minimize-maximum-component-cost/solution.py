from typing import List

class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node: int) -> int:
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, node1: int, node2: int) -> bool:
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2:
            return False

        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

        return True


class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        def get_weight(edge: List[int]) -> int:
            return edge[2]

        edges.sort(key=get_weight)
        union_find = UnionFind(n)
        mst_edges = []

        for node1, node2, weight in edges:
            if union_find.union(node1, node2):
                mst_edges.append((node1, node2, weight))
                if len(mst_edges) == n - 1:
                    break

        if k >= n:
            return 0

        mst_edges.sort(key=get_weight, reverse=True)

        for removal_round in range(k - 1):
            if mst_edges:
                mst_edges.pop(0)

        max_weight = 0
        for node1, node2, weight in mst_edges:
            max_weight = max(max_weight, weight)

        return max_weight

