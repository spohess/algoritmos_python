import random
from solution import max_subarray_sum


class TestMaxSubarraySum:
    def test_basic(self):
        assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    def test_all_negative(self):
        assert max_subarray_sum([-3, -2, -5, -1]) == -1

    def test_all_positive(self):
        assert max_subarray_sum([1, 2, 3, 4]) == 10

    def test_single_element(self):
        assert max_subarray_sum([5]) == 5
        assert max_subarray_sum([-5]) == -5

    def test_zeros(self):
        assert max_subarray_sum([0, 0, 0]) == 0

    def test_mixed(self):
        assert max_subarray_sum([1, -1, 1, -1, 1]) == 1

    def test_random_oracle(self):
        random.seed(42)
        for _ in range(50):
            size = random.randint(1, 100)
            nums = [random.randint(-50, 50) for _ in range(size)]
            # brute force O(n^2)
            expected = nums[0]
            for i in range(len(nums)):
                s = 0
                for j in range(i, len(nums)):
                    s += nums[j]
                    expected = max(expected, s)
            assert max_subarray_sum(nums) == expected
