import random
from solution import intersection


class TestIntersection:
    def test_basic(self):
        result = intersection([1, 2, 2, 3], [2, 3, 4])
        assert sorted(result) == [2, 3]

    def test_no_common(self):
        result = intersection([1, 2], [3, 4])
        assert result == []

    def test_empty_first(self):
        result = intersection([], [1, 2])
        assert result == []

    def test_empty_second(self):
        result = intersection([1, 2], [])
        assert result == []

    def test_both_empty(self):
        result = intersection([], [])
        assert result == []

    def test_identical(self):
        result = intersection([1, 2, 3], [1, 2, 3])
        assert sorted(result) == [1, 2, 3]

    def test_duplicates_in_input(self):
        result = intersection([1, 1, 1], [1, 1])
        assert result == [1]

    def test_no_duplicates_in_result(self):
        result = intersection([2, 2, 2], [2, 2])
        assert result == [2]

    def test_random_oracle(self):
        random.seed(42)
        for _ in range(50):
            s1 = random.randint(0, 100)
            s2 = random.randint(0, 100)
            nums1 = [random.randint(-20, 20) for _ in range(s1)]
            nums2 = [random.randint(-20, 20) for _ in range(s2)]
            expected = sorted(set(nums1) & set(nums2))
            assert sorted(intersection(nums1, nums2)) == expected
