import random
from solution import merge_intervals


class TestMergeIntervals:
    def test_basic(self):
        assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
            [1, 6],
            [8, 10],
            [15, 18],
        ]

    def test_overlap_all(self):
        assert merge_intervals([[1, 4], [2, 5], [3, 6]]) == [[1, 6]]

    def test_no_overlap(self):
        assert merge_intervals([[1, 2], [4, 5], [7, 8]]) == [[1, 2], [4, 5], [7, 8]]

    def test_empty(self):
        assert merge_intervals([]) == []

    def test_single(self):
        assert merge_intervals([[1, 5]]) == [[1, 5]]

    def test_adjacent(self):
        assert merge_intervals([[1, 2], [2, 3]]) == [[1, 3]]

    def test_unsorted_input(self):
        assert merge_intervals([[3, 4], [1, 2], [2, 3]]) == [[1, 4]]

    def test_contained(self):
        assert merge_intervals([[1, 10], [2, 5], [3, 7]]) == [[1, 10]]

    def test_random_oracle(self):
        random.seed(42)
        for _ in range(50):
            n = random.randint(0, 30)
            intervals = []
            for _ in range(n):
                a = random.randint(0, 100)
                b = a + random.randint(0, 20)
                intervals.append([a, b])
            # brute force
            if not intervals:
                expected = []
            else:
                s = sorted(intervals, key=lambda x: x[0])
                expected = [s[0][:]]
                for start, end in s[1:]:
                    if start <= expected[-1][1]:
                        expected[-1][1] = max(expected[-1][1], end)
                    else:
                        expected.append([start, end])
            assert merge_intervals(intervals) == expected
