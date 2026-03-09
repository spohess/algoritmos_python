import random
import string
from solution import longest_common_prefix


class TestLongestCommonPrefix:
    def test_basic(self):
        assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"

    def test_no_common(self):
        assert longest_common_prefix(["dog", "car", "race"]) == ""

    def test_empty_list(self):
        assert longest_common_prefix([]) == ""

    def test_single_string(self):
        assert longest_common_prefix(["hello"]) == "hello"

    def test_all_identical(self):
        assert longest_common_prefix(["abc", "abc", "abc"]) == "abc"

    def test_empty_string_in_list(self):
        assert longest_common_prefix(["abc", "", "abd"]) == ""

    def test_single_char_common(self):
        assert longest_common_prefix(["a", "ab", "ac"]) == "a"

    def test_random_oracle(self):
        random.seed(42)
        for _ in range(50):
            prefix = "".join(random.choices(string.ascii_lowercase, k=random.randint(0, 5)))
            n = random.randint(1, 10)
            strs = [
                prefix + "".join(random.choices(string.ascii_lowercase, k=random.randint(0, 10)))
                for _ in range(n)
            ]
            # brute force
            if not strs:
                expected = ""
            else:
                expected = strs[0]
                for s in strs[1:]:
                    while not s.startswith(expected):
                        expected = expected[:-1]
                        if not expected:
                            break
            assert longest_common_prefix(strs) == expected
