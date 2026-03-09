import random
from solution import is_valid_parentheses


class TestIsValidParentheses:
    def test_basic_valid(self):
        assert is_valid_parentheses("()[]{}") is True

    def test_nested(self):
        assert is_valid_parentheses("{[()]}") is True

    def test_invalid_order(self):
        assert is_valid_parentheses("([)]") is False

    def test_only_open(self):
        assert is_valid_parentheses("(((") is False

    def test_only_close(self):
        assert is_valid_parentheses(")))") is False

    def test_empty(self):
        assert is_valid_parentheses("") is True

    def test_single_open(self):
        assert is_valid_parentheses("(") is False

    def test_single_close(self):
        assert is_valid_parentheses(")") is False

    def test_complex_valid(self):
        assert is_valid_parentheses("({[]})()[]") is True

    def test_close_without_open(self):
        assert is_valid_parentheses("())") is False

    def test_random_oracle(self):
        random.seed(42)
        pairs = {"(": ")", "[": "]", "{": "}"}
        closing = set(pairs.values())
        for _ in range(100):
            size = random.randint(0, 30)
            chars = list("()[]{}")
            s = "".join(random.choices(chars, k=size))
            # brute force with stack
            stack = []
            expected = True
            for c in s:
                if c in pairs:
                    stack.append(pairs[c])
                elif c in closing:
                    if not stack or stack[-1] != c:
                        expected = False
                        break
                    stack.pop()
            if stack:
                expected = False
            assert is_valid_parentheses(s) is expected
