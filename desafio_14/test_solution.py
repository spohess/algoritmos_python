import random
from solution import max_sum_window


class TestMaxSumWindow:
    def test_basic(self):
        assert max_sum_window([1, 3, -1, 2, 5, 1], 3) == 8

    def test_k_equals_length(self):
        assert max_sum_window([1, 2, 3], 3) == 6

    def test_k_one(self):
        assert max_sum_window([1, -2, 3, -1], 1) == 3

    def test_all_equal(self):
        assert max_sum_window([5, 5, 5, 5], 2) == 10

    def test_all_negative(self):
        assert max_sum_window([-1, -2, -3, -4], 2) == -3

    def test_single_element(self):
        assert max_sum_window([7], 1) == 7

    def test_random_oracle(self):
        random.seed(42)
        for _ in range(50):
            size = random.randint(1, 100)
            nums = [random.randint(-50, 50) for _ in range(size)]
            k = random.randint(1, size)
            # brute force
            expected = max(sum(nums[i : i + k]) for i in range(size - k + 1))
            assert max_sum_window(nums, k) == expected
