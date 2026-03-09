import random
from solution import rotate_array


class TestRotateArray:
    def test_basic(self):
        assert rotate_array([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

    def test_k_zero(self):
        assert rotate_array([1, 2, 3], 0) == [1, 2, 3]

    def test_k_equals_length(self):
        assert rotate_array([1, 2, 3], 3) == [1, 2, 3]

    def test_k_greater_than_length(self):
        assert rotate_array([1, 2, 3], 5) == [2, 3, 1]

    def test_empty(self):
        assert rotate_array([], 3) == []

    def test_single_element(self):
        assert rotate_array([1], 10) == [1]

    def test_k_one(self):
        assert rotate_array([1, 2, 3, 4], 1) == [4, 1, 2, 3]

    def test_random_oracle(self):
        random.seed(42)
        for _ in range(50):
            size = random.randint(0, 100)
            nums = [random.randint(-100, 100) for _ in range(size)]
            k = random.randint(0, 200)
            # brute force
            if not nums:
                expected = []
            else:
                r = k % len(nums)
                expected = nums[-r:] + nums[:-r] if r else nums[:]
            assert rotate_array(nums, k) == expected
