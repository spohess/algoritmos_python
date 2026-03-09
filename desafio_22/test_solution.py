import random
from solution import kth_smallest


class TestKthSmallest:
    def test_basic(self):
        assert kth_smallest([3, 1, 2, 4, 5], 2) == 2

    def test_first(self):
        assert kth_smallest([7, 3, 5, 1], 1) == 1

    def test_last(self):
        assert kth_smallest([7, 3, 5, 1], 4) == 7

    def test_duplicates(self):
        assert kth_smallest([3, 3, 3, 1, 1], 3) == 3

    def test_single(self):
        assert kth_smallest([42], 1) == 42

    def test_sorted(self):
        assert kth_smallest([1, 2, 3, 4, 5], 3) == 3

    def test_reverse_sorted(self):
        assert kth_smallest([5, 4, 3, 2, 1], 3) == 3

    def test_negatives(self):
        assert kth_smallest([-5, -1, -3, 0, 2], 2) == -3

    def test_random_oracle(self):
        random.seed(42)
        for _ in range(50):
            size = random.randint(1, 200)
            nums = [random.randint(-100, 100) for _ in range(size)]
            k = random.randint(1, size)
            expected = sorted(nums)[k - 1]
            assert kth_smallest(nums[:], k) == expected
