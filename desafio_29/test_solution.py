import random
from solution import length_of_lis


def _lis_oracle(nums):
    if not nums:
        return 0
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


class TestLengthOfLIS:
    def test_basic(self):
        assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4

    def test_increasing(self):
        assert length_of_lis([1, 2, 3, 4, 5]) == 5

    def test_decreasing(self):
        assert length_of_lis([5, 4, 3, 2, 1]) == 1

    def test_empty(self):
        assert length_of_lis([]) == 0

    def test_single(self):
        assert length_of_lis([7]) == 1

    def test_all_equal(self):
        assert length_of_lis([3, 3, 3, 3]) == 1

    def test_negatives(self):
        assert length_of_lis([-5, -3, -1, 0, 2]) == 5

    def test_mixed(self):
        assert length_of_lis([0, 1, 0, 3, 2, 3]) == 4

    def test_random_oracle(self):
        random.seed(42)
        for _ in range(50):
            size = random.randint(0, 80)
            nums = [random.randint(-50, 50) for _ in range(size)]
            expected = _lis_oracle(nums)
            assert length_of_lis(nums) == expected
