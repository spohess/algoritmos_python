import random
from solution import product_except_self


class TestProductExceptSelf:
    def test_basic(self):
        assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]

    def test_with_zero(self):
        assert product_except_self([1, 2, 0, 4]) == [0, 0, 8, 0]

    def test_multiple_zeros(self):
        assert product_except_self([0, 0, 2]) == [0, 0, 0]

    def test_two_elements(self):
        assert product_except_self([3, 5]) == [5, 3]

    def test_negatives(self):
        assert product_except_self([-1, 2, -3]) == [-6, 3, -2]

    def test_all_ones(self):
        assert product_except_self([1, 1, 1, 1]) == [1, 1, 1, 1]

    def test_random_oracle(self):
        random.seed(42)
        for _ in range(50):
            size = random.randint(2, 50)
            nums = [random.randint(-10, 10) for _ in range(size)]
            # brute force
            expected = []
            for i in range(len(nums)):
                p = 1
                for j in range(len(nums)):
                    if j != i:
                        p *= nums[j]
                expected.append(p)
            assert product_except_self(nums) == expected
