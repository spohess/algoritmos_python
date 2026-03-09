from solution import topological_sort


def _is_valid_topo_order(n, edges, order):
    if len(order) != n:
        return False
    if set(order) != set(range(n)):
        return False
    pos = {v: i for i, v in enumerate(order)}
    for u, v in edges:
        if pos[u] >= pos[v]:
            return False
    return True


class TestTopologicalSort:
    def test_basic(self):
        result = topological_sort(4, [[0, 1], [0, 2], [1, 3], [2, 3]])
        assert _is_valid_topo_order(4, [[0, 1], [0, 2], [1, 3], [2, 3]], result)

    def test_linear(self):
        result = topological_sort(3, [[0, 1], [1, 2]])
        assert _is_valid_topo_order(3, [[0, 1], [1, 2]], result)

    def test_no_edges(self):
        result = topological_sort(3, [])
        assert _is_valid_topo_order(3, [], result)

    def test_cycle(self):
        result = topological_sort(3, [[0, 1], [1, 2], [2, 0]])
        assert result == []

    def test_self_loop(self):
        result = topological_sort(2, [[0, 0]])
        assert result == []

    def test_single_node(self):
        result = topological_sort(1, [])
        assert result == [0]

    def test_two_nodes_no_edge(self):
        result = topological_sort(2, [])
        assert _is_valid_topo_order(2, [], result)

    def test_diamond(self):
        edges = [[0, 1], [0, 2], [1, 3], [2, 3]]
        result = topological_sort(4, edges)
        assert _is_valid_topo_order(4, edges, result)

    def test_complex(self):
        edges = [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]
        result = topological_sort(6, edges)
        assert _is_valid_topo_order(6, edges, result)

    def test_two_node_cycle(self):
        result = topological_sort(2, [[0, 1], [1, 0]])
        assert result == []
