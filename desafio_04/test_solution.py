import random
import string
from solution import first_unique_char


class TestFirstUniqueChar:
    def test_basic(self):
        assert first_unique_char("abacabad") == "c"

    def test_first_char_unique(self):
        assert first_unique_char("abcdef") == "a"

    def test_last_char_unique(self):
        assert first_unique_char("aabbccd") == "d"

    def test_no_unique(self):
        assert first_unique_char("aabbcc") == ""

    def test_empty(self):
        assert first_unique_char("") == ""

    def test_single_char(self):
        assert first_unique_char("z") == "z"

    def test_all_same(self):
        assert first_unique_char("aaaa") == ""

    def test_random_oracle(self):
        random.seed(42)
        for _ in range(50):
            size = random.randint(0, 100)
            s = "".join(random.choices(string.ascii_lowercase[:5], k=size))
            # brute force
            expected = ""
            for ch in s:
                if s.count(ch) == 1:
                    expected = ch
                    break
            assert first_unique_char(s) == expected
