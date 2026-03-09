from solution import TreeNode, lowest_common_ancestor


def _find_node(root: TreeNode | None, val: int) -> TreeNode | None:
    if root is None:
        return None
    if root.val == val:
        return root
    return _find_node(root.left, val) or _find_node(root.right, val)


class TestLowestCommonAncestor:
    def _build_sample_tree(self):
        #        3
        #       / \
        #      5   1
        #     / \ / \
        #    6  2 0  8
        #      / \
        #     7   4
        n7 = TreeNode(7)
        n4 = TreeNode(4)
        n2 = TreeNode(2, n7, n4)
        n6 = TreeNode(6)
        n5 = TreeNode(5, n6, n2)
        n0 = TreeNode(0)
        n8 = TreeNode(8)
        n1 = TreeNode(1, n0, n8)
        n3 = TreeNode(3, n5, n1)
        return n3

    def test_basic(self):
        root = self._build_sample_tree()
        p = _find_node(root, 5)
        q = _find_node(root, 1)
        assert lowest_common_ancestor(root, p, q).val == 3

    def test_ancestor_is_one_of_nodes(self):
        root = self._build_sample_tree()
        p = _find_node(root, 5)
        q = _find_node(root, 4)
        assert lowest_common_ancestor(root, p, q).val == 5

    def test_same_side(self):
        root = self._build_sample_tree()
        p = _find_node(root, 6)
        q = _find_node(root, 4)
        assert lowest_common_ancestor(root, p, q).val == 5

    def test_opposite_sides(self):
        root = self._build_sample_tree()
        p = _find_node(root, 6)
        q = _find_node(root, 8)
        assert lowest_common_ancestor(root, p, q).val == 3

    def test_root_is_answer(self):
        root = self._build_sample_tree()
        p = _find_node(root, 7)
        q = _find_node(root, 0)
        assert lowest_common_ancestor(root, p, q).val == 3

    def test_two_nodes(self):
        root = TreeNode(1, TreeNode(2))
        p = root
        q = root.left
        assert lowest_common_ancestor(root, p, q).val == 1

    def test_deep_nodes(self):
        root = self._build_sample_tree()
        p = _find_node(root, 7)
        q = _find_node(root, 4)
        assert lowest_common_ancestor(root, p, q).val == 2
