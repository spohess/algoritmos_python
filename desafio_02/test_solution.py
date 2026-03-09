import random
from solution import longest_continuous_increasing


class TestLongestContinuousIncreasing:
    def test_basic(self):
        assert longest_continuous_increasing([1, 3, 5, 4, 7]) == 3

    def test_decreasing(self):
        assert longest_continuous_increasing([5, 4, 3, 2, 1]) == 1

    def test_all_equal(self):
        assert longest_continuous_increasing([2, 2, 2, 2]) == 1

    def test_empty(self):
        assert longest_continuous_increasing([]) == 0

    def test_single(self):
        assert longest_continuous_increasing([10]) == 1

    def test_fully_increasing(self):
        assert longest_continuous_increasing([1, 2, 3, 4, 5]) == 5

    def test_increasing_at_end(self):
        assert longest_continuous_increasing([5, 1, 2, 3, 4]) == 4

    def test_two_sequences(self):
        assert longest_continuous_increasing([1, 2, 3, 1, 2, 3, 4]) == 4

    def test_random_oracle(self):
        random.seed(42)
        for _ in range(50):
            size = random.randint(0, 200)
            nums = [random.randint(-50, 50) for _ in range(size)]
            # brute force
            if not nums:
                expected = 0
            else:
                max_len = 1
                cur_len = 1
                for i in range(1, len(nums)):
                    if nums[i] > nums[i - 1]:
                        cur_len += 1
                    else:
                        cur_len = 1
                    max_len = max(max_len, cur_len)
                expected = max_len
            assert longest_continuous_increasing(nums) == expected
