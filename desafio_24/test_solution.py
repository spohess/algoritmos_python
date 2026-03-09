from collections import deque
from solution import TreeNode, invert_tree


def _build_tree(values: list) -> TreeNode | None:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def _tree_to_list(root: TreeNode | None) -> list:
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


class TestInvertTree:
    def test_basic(self):
        root = _build_tree([4, 2, 7, 1, 3, 6, 9])
        result = invert_tree(root)
        assert _tree_to_list(result) == [4, 7, 2, 9, 6, 3, 1]

    def test_empty(self):
        assert invert_tree(None) is None

    def test_single_node(self):
        root = TreeNode(1)
        result = invert_tree(root)
        assert _tree_to_list(result) == [1]

    def test_left_only(self):
        root = _build_tree([1, 2, None])
        result = invert_tree(root)
        assert _tree_to_list(result) == [1, None, 2]

    def test_right_only(self):
        root = _build_tree([1, None, 2])
        result = invert_tree(root)
        assert _tree_to_list(result) == [1, 2]

    def test_two_levels(self):
        root = _build_tree([1, 2, 3])
        result = invert_tree(root)
        assert _tree_to_list(result) == [1, 3, 2]

    def test_double_invert(self):
        values = [4, 2, 7, 1, 3, 6, 9]
        root = _build_tree(values)
        result = invert_tree(invert_tree(root))
        assert _tree_to_list(result) == values
