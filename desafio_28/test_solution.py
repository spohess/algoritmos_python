import random
from solution import coin_change


def _coin_change_oracle(coins, amount):
    if amount == 0:
        return 0
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            if c <= i and dp[i - c] + 1 < dp[i]:
                dp[i] = dp[i - c] + 1
    return dp[amount] if dp[amount] != float("inf") else -1


class TestCoinChange:
    def test_basic(self):
        assert coin_change([1, 5, 10, 25], 30) == 2

    def test_impossible(self):
        assert coin_change([2], 3) == -1

    def test_zero_amount(self):
        assert coin_change([1, 2, 3], 0) == 0

    def test_single_coin(self):
        assert coin_change([3], 9) == 3

    def test_exact_denomination(self):
        assert coin_change([1, 5, 10], 10) == 1

    def test_one_coin_denomination(self):
        assert coin_change([1], 7) == 7

    def test_large_amount(self):
        assert coin_change([1, 5, 10, 25], 100) == 4

    def test_unsorted_coins(self):
        assert coin_change([5, 1, 10], 11) == 2

    def test_random_oracle(self):
        random.seed(42)
        for _ in range(30):
            n_coins = random.randint(1, 5)
            coins = list(set(random.randint(1, 20) for _ in range(n_coins)))
            if not coins:
                coins = [1]
            amount = random.randint(0, 100)
            expected = _coin_change_oracle(coins, amount)
            assert coin_change(coins, amount) == expected
