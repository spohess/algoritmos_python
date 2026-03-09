import random
import string
from solution import is_anagram


class TestIsAnagram:
    def test_basic_anagram(self):
        assert is_anagram("listen", "silent") is True

    def test_not_anagram(self):
        assert is_anagram("hello", "world") is False

    def test_ignore_case(self):
        assert is_anagram("Triangle", "Integral") is True

    def test_ignore_spaces(self):
        assert is_anagram("a gentleman", "elegant man") is True

    def test_empty_strings(self):
        assert is_anagram("", "") is True

    def test_only_spaces(self):
        assert is_anagram("   ", "  ") is True

    def test_different_lengths(self):
        assert is_anagram("abc", "abcd") is False

    def test_single_char(self):
        assert is_anagram("a", "A") is True

    def test_numbers_in_string(self):
        assert is_anagram("abc123", "321cba") is True

    def test_random_oracle(self):
        random.seed(42)
        for _ in range(50):
            size = random.randint(0, 50)
            chars = random.choices(string.ascii_lowercase, k=size)
            s1 = "".join(chars)
            if random.random() < 0.5:
                shuffled = chars[:]
                random.shuffle(shuffled)
                s2 = "".join(shuffled)
            else:
                s2 = "".join(random.choices(string.ascii_lowercase, k=size))
            # brute force
            clean1 = sorted(s1.replace(" ", "").lower())
            clean2 = sorted(s2.replace(" ", "").lower())
            expected = clean1 == clean2
            assert is_anagram(s1, s2) is expected
