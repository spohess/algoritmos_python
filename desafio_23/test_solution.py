from solution import ListNode, has_cycle


def _make_list(values: list[int], cycle_index: int = -1) -> ListNode | None:
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if cycle_index >= 0:
        nodes[-1].next = nodes[cycle_index]
    return nodes[0]


class TestHasCycle:
    def test_no_cycle(self):
        head = _make_list([1, 2, 3, 4])
        assert has_cycle(head) is False

    def test_cycle_to_start(self):
        head = _make_list([1, 2, 3, 4], cycle_index=0)
        assert has_cycle(head) is True

    def test_cycle_to_middle(self):
        head = _make_list([1, 2, 3, 4, 5], cycle_index=2)
        assert has_cycle(head) is True

    def test_self_cycle(self):
        head = _make_list([1], cycle_index=0)
        assert has_cycle(head) is True

    def test_empty(self):
        assert has_cycle(None) is False

    def test_single_no_cycle(self):
        head = _make_list([1])
        assert has_cycle(head) is False

    def test_two_nodes_cycle(self):
        head = _make_list([1, 2], cycle_index=0)
        assert has_cycle(head) is True

    def test_two_nodes_no_cycle(self):
        head = _make_list([1, 2])
        assert has_cycle(head) is False

    def test_cycle_at_last(self):
        head = _make_list([1, 2, 3, 4, 5], cycle_index=4)
        assert has_cycle(head) is True
