import random
import string
from solution import is_palindrome


class TestIsPalindrome:
    def test_basic_palindrome(self):
        assert is_palindrome("A man, a plan, a canal: Panama") is True

    def test_not_palindrome(self):
        assert is_palindrome("race a car") is False

    def test_empty(self):
        assert is_palindrome("") is True

    def test_only_symbols(self):
        assert is_palindrome("!@#$%") is True

    def test_single_char(self):
        assert is_palindrome("a") is True

    def test_numbers(self):
        assert is_palindrome("12321") is True

    def test_mixed_case(self):
        assert is_palindrome("Aa") is True

    def test_spaces_only(self):
        assert is_palindrome("   ") is True

    def test_not_palindrome_simple(self):
        assert is_palindrome("ab") is False

    def test_random_oracle(self):
        random.seed(42)
        for _ in range(50):
            size = random.randint(0, 50)
            s = "".join(random.choices(string.ascii_letters + string.digits + " !@#.,", k=size))
            # brute force
            cleaned = "".join(c.lower() for c in s if c.isalnum())
            expected = cleaned == cleaned[::-1]
            assert is_palindrome(s) is expected
