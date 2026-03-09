import random
import string
from collections import Counter
from solution import min_window_substring


def _contains_all(window: str, t: str) -> bool:
    tc = Counter(t)
    wc = Counter(window)
    return all(wc[c] >= tc[c] for c in tc)


class TestMinWindowSubstring:
    def test_basic(self):
        result = min_window_substring("ADOBECODEBANC", "ABC")
        assert _contains_all(result, "ABC")
        assert len(result) == 4

    def test_exact_match(self):
        result = min_window_substring("abc", "abc")
        assert _contains_all(result, "abc")
        assert len(result) == 3

    def test_no_match(self):
        assert min_window_substring("abc", "xyz") == ""

    def test_s_shorter_than_t(self):
        assert min_window_substring("ab", "abc") == ""

    def test_t_empty(self):
        assert min_window_substring("abc", "") == ""

    def test_duplicate_in_t(self):
        result = min_window_substring("aabbc", "aab")
        assert _contains_all(result, "aab")

    def test_single_char(self):
        result = min_window_substring("abcdef", "d")
        assert result == "d"

    def test_random_oracle(self):
        random.seed(42)
        for _ in range(30):
            slen = random.randint(1, 60)
            tlen = random.randint(0, 10)
            alphabet = string.ascii_lowercase[:5]
            s = "".join(random.choices(alphabet, k=slen))
            t = "".join(random.choices(alphabet, k=tlen))
            result = min_window_substring(s, t)
            if not t:
                assert result == ""
                continue
            # brute force: find minimum window
            best = None
            for i in range(len(s)):
                for j in range(i + 1, len(s) + 1):
                    w = s[i:j]
                    if _contains_all(w, t):
                        if best is None or len(w) < len(best):
                            best = w
                        break
            if best is None:
                assert result == ""
            else:
                assert _contains_all(result, t)
                assert len(result) == len(best)
