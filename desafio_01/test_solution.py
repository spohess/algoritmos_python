import random
from solution import has_pair_with_sum


class TestHasPairWithSum:
    def test_pair_exists(self):
        assert has_pair_with_sum([1, 2, 3, 4], 5) is True

    def test_pair_not_exists(self):
        assert has_pair_with_sum([1, 2, 3, 4], 10) is False

    def test_empty_array(self):
        assert has_pair_with_sum([], 5) is False

    def test_single_element(self):
        assert has_pair_with_sum([5], 5) is False

    def test_negative_numbers(self):
        assert has_pair_with_sum([-1, -2, 3, 7], 1) is True

    def test_zero_target(self):
        assert has_pair_with_sum([-3, 1, 3, 0], 0) is True

    def test_duplicates_needed(self):
        assert has_pair_with_sum([3, 3], 6) is True

    def test_single_element_not_double(self):
        assert has_pair_with_sum([3], 6) is False

    def test_all_zeros(self):
        assert has_pair_with_sum([0, 0, 0], 0) is True

    def test_large_numbers(self):
        assert has_pair_with_sum([10**9, -(10**9)], 0) is True

    def test_random_oracle(self):
        random.seed(42)
        for _ in range(50):
            size = random.randint(0, 100)
            nums = [random.randint(-100, 100) for _ in range(size)]
            target = random.randint(-200, 200)
            # brute force oracle
            expected = False
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if nums[i] + nums[j] == target:
                        expected = True
                        break
                if expected:
                    break
            assert has_pair_with_sum(nums, target) is expected
