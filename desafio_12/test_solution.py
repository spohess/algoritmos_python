import random
from solution import two_sum_sorted


class TestTwoSumSorted:
    def test_basic(self):
        result = two_sum_sorted([1, 2, 3, 4, 6], 6)
        i, j = result
        assert i < j
        assert [1, 2, 3, 4, 6][i] + [1, 2, 3, 4, 6][j] == 6

    def test_not_found(self):
        assert two_sum_sorted([1, 2, 3], 10) == (-1, -1)

    def test_two_elements(self):
        assert two_sum_sorted([1, 4], 5) == (0, 1)

    def test_negative(self):
        result = two_sum_sorted([-3, -1, 0, 2, 5], -4)
        i, j = result
        assert [-3, -1, 0, 2, 5][i] + [-3, -1, 0, 2, 5][j] == -4

    def test_duplicates(self):
        result = two_sum_sorted([1, 1, 2, 3], 2)
        i, j = result
        assert i < j
        assert [1, 1, 2, 3][i] + [1, 1, 2, 3][j] == 2

    def test_random_oracle(self):
        random.seed(42)
        for _ in range(50):
            size = random.randint(2, 100)
            nums = sorted(random.randint(-50, 50) for _ in range(size))
            target = random.randint(-100, 100)
            result = two_sum_sorted(nums, target)
            # brute force check
            found = False
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if nums[i] + nums[j] == target:
                        found = True
                        break
                if found:
                    break
            if found:
                i, j = result
                assert i < j and i >= 0
                assert nums[i] + nums[j] == target
            else:
                assert result == (-1, -1)
