from collections import deque
from solution import shortest_path_grid


def _bfs_oracle(grid):
    if not grid or not grid[0]:
        return -1
    rows, cols = len(grid), len(grid[0])
    if rows == 1 and cols == 1:
        return 0
    visited = [[False] * cols for _ in range(rows)]
    visited[0][0] = True
    queue = deque([(0, 0, 0)])
    while queue:
        r, c, d = queue.popleft()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == 0:
                if nr == rows - 1 and nc == cols - 1:
                    return d + 1
                visited[nr][nc] = True
                queue.append((nr, nc, d + 1))
    return -1


class TestShortestPathGrid:
    def test_basic(self):
        grid = [
            [0, 0, 0],
            [1, 1, 0],
            [0, 0, 0],
        ]
        assert shortest_path_grid(grid) == 4

    def test_no_path(self):
        grid = [
            [0, 1],
            [1, 0],
        ]
        assert shortest_path_grid(grid) == -1

    def test_single_cell(self):
        assert shortest_path_grid([[0]]) == 0

    def test_straight_path(self):
        grid = [
            [0, 0, 0, 0],
        ]
        assert shortest_path_grid(grid) == 3

    def test_no_obstacles(self):
        grid = [
            [0, 0],
            [0, 0],
        ]
        assert shortest_path_grid(grid) == 2

    def test_larger_grid(self):
        grid = [
            [0, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0],
        ]
        result = shortest_path_grid(grid)
        expected = _bfs_oracle(grid)
        assert result == expected

    def test_maze(self):
        grid = [
            [0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 0],
        ]
        result = shortest_path_grid(grid)
        expected = _bfs_oracle(grid)
        assert result == expected
