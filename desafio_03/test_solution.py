import random
from solution import remove_duplicates


class TestRemoveDuplicates:
    def test_basic(self):
        assert remove_duplicates([1, 2, 3, 2, 1]) == [1, 2, 3]

    def test_empty(self):
        assert remove_duplicates([]) == []

    def test_no_duplicates(self):
        assert remove_duplicates([1, 2, 3]) == [1, 2, 3]

    def test_all_same(self):
        assert remove_duplicates([5, 5, 5, 5]) == [5]

    def test_preserves_order(self):
        assert remove_duplicates([3, 1, 2, 1, 3, 2]) == [3, 1, 2]

    def test_single_element(self):
        assert remove_duplicates([7]) == [7]

    def test_negative_numbers(self):
        assert remove_duplicates([-1, -2, -1, -3, -2]) == [-1, -2, -3]

    def test_random_oracle(self):
        random.seed(42)
        for _ in range(50):
            size = random.randint(0, 200)
            nums = [random.randint(-20, 20) for _ in range(size)]
            # brute force
            seen = set()
            expected = []
            for x in nums:
                if x not in seen:
                    seen.add(x)
                    expected.append(x)
            assert remove_duplicates(nums) == expected
