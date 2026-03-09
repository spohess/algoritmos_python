import random
import string
from solution import edit_distance


def _edit_distance_oracle(w1, w2):
    m, n = len(w1), len(w2)
    dp = list(range(n + 1))
    for i in range(1, m + 1):
        prev = dp[0]
        dp[0] = i
        for j in range(1, n + 1):
            temp = dp[j]
            if w1[i - 1] == w2[j - 1]:
                dp[j] = prev
            else:
                dp[j] = 1 + min(prev, dp[j], dp[j - 1])
            prev = temp
    return dp[n]


class TestEditDistance:
    def test_basic(self):
        assert edit_distance("horse", "ros") == 3

    def test_longer(self):
        assert edit_distance("intention", "execution") == 5

    def test_equal(self):
        assert edit_distance("abc", "abc") == 0

    def test_empty_first(self):
        assert edit_distance("", "abc") == 3

    def test_empty_second(self):
        assert edit_distance("abc", "") == 3

    def test_both_empty(self):
        assert edit_distance("", "") == 0

    def test_single_char_same(self):
        assert edit_distance("a", "a") == 0

    def test_single_char_diff(self):
        assert edit_distance("a", "b") == 1

    def test_prefix(self):
        assert edit_distance("abc", "abcdef") == 3

    def test_completely_different(self):
        assert edit_distance("abc", "xyz") == 3

    def test_random_oracle(self):
        random.seed(42)
        for _ in range(50):
            len1 = random.randint(0, 30)
            len2 = random.randint(0, 30)
            w1 = "".join(random.choices(string.ascii_lowercase[:5], k=len1))
            w2 = "".join(random.choices(string.ascii_lowercase[:5], k=len2))
            expected = _edit_distance_oracle(w1, w2)
            assert edit_distance(w1, w2) == expected
