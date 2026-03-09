import random
from solution import find_interval


class TestFindInterval:
    def test_basic(self):
        intervals = [[1, 3], [5, 7], [9, 12]]
        assert find_interval(intervals, 6) == 1

    def test_not_found(self):
        intervals = [[1, 3], [5, 7], [9, 12]]
        assert find_interval(intervals, 4) == -1

    def test_empty(self):
        assert find_interval([], 5) == -1

    def test_at_start(self):
        intervals = [[1, 3], [5, 7]]
        assert find_interval(intervals, 1) == 0

    def test_at_end(self):
        intervals = [[1, 3], [5, 7]]
        assert find_interval(intervals, 3) == 0

    def test_before_all(self):
        intervals = [[5, 10], [15, 20]]
        assert find_interval(intervals, 2) == -1

    def test_after_all(self):
        intervals = [[5, 10], [15, 20]]
        assert find_interval(intervals, 25) == -1

    def test_single_interval(self):
        assert find_interval([[3, 8]], 5) == 0
        assert find_interval([[3, 8]], 2) == -1

    def test_random_oracle(self):
        random.seed(42)
        for _ in range(50):
            n = random.randint(0, 20)
            intervals = []
            pos = 0
            for _ in range(n):
                start = pos + random.randint(1, 5)
                end = start + random.randint(1, 10)
                intervals.append([start, end])
                pos = end
            point = random.randint(-5, pos + 10)
            # brute force
            expected = -1
            for i, (s, e) in enumerate(intervals):
                if s <= point <= e:
                    expected = i
                    break
            assert find_interval(intervals, point) == expected
