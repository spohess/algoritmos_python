import heapq
from solution import dijkstra


def _dijkstra_oracle(n, edges, src):
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
    dist = [-1] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if dist[v] == -1 or nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist


class TestDijkstra:
    def test_basic(self):
        edges = [[0, 1, 4], [0, 2, 1], [2, 1, 2], [1, 3, 1], [2, 3, 5]]
        assert dijkstra(4, edges, 0) == [0, 3, 1, 4]

    def test_unreachable(self):
        edges = [[0, 1, 1]]
        assert dijkstra(3, edges, 0) == [0, 1, -1]

    def test_single_node(self):
        assert dijkstra(1, [], 0) == [0]

    def test_no_edges(self):
        assert dijkstra(3, [], 0) == [0, -1, -1]

    def test_zero_weight(self):
        edges = [[0, 1, 0], [1, 2, 0]]
        assert dijkstra(3, edges, 0) == [0, 0, 0]

    def test_multiple_paths(self):
        edges = [[0, 1, 10], [0, 2, 3], [2, 1, 1], [1, 3, 2], [2, 3, 8]]
        result = dijkstra(4, edges, 0)
        expected = _dijkstra_oracle(4, edges, 0)
        assert result == expected

    def test_larger_graph(self):
        edges = [
            [0, 1, 7], [0, 2, 9], [0, 5, 14],
            [1, 2, 10], [1, 3, 15],
            [2, 3, 11], [2, 5, 2],
            [3, 4, 6],
            [4, 5, 9],
        ]
        result = dijkstra(6, edges, 0)
        expected = _dijkstra_oracle(6, edges, 0)
        assert result == expected
