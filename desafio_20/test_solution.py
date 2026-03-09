from solution import count_islands


def _count_oracle(grid):
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and not visited[i][j]:
                count += 1
                stack = [(i, j)]
                visited[i][j] = True
                while stack:
                    r, c = stack.pop()
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
    return count


class TestCountIslands:
    def test_basic(self):
        grid = [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1],
        ]
        assert count_islands(grid) == 3

    def test_single_island(self):
        grid = [
            [1, 1, 1],
            [1, 1, 1],
        ]
        assert count_islands(grid) == 1

    def test_no_island(self):
        grid = [
            [0, 0],
            [0, 0],
        ]
        assert count_islands(grid) == 0

    def test_empty(self):
        assert count_islands([]) == 0

    def test_single_cell_land(self):
        assert count_islands([[1]]) == 1

    def test_single_cell_water(self):
        assert count_islands([[0]]) == 0

    def test_diagonal_not_connected(self):
        grid = [
            [1, 0],
            [0, 1],
        ]
        assert count_islands(grid) == 2

    def test_all_land(self):
        grid = [
            [1, 1],
            [1, 1],
        ]
        assert count_islands(grid) == 1

    def test_checkerboard(self):
        grid = [
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1],
        ]
        assert count_islands(grid) == 5
