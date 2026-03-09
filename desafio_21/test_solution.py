import random
from collections import Counter
from solution import top_k_frequent


class TestTopKFrequent:
    def test_basic(self):
        result = top_k_frequent([1, 1, 1, 2, 2, 3], 2)
        assert sorted(result) == [1, 2]

    def test_single(self):
        result = top_k_frequent([1], 1)
        assert result == [1]

    def test_all_same(self):
        result = top_k_frequent([5, 5, 5], 1)
        assert result == [5]

    def test_k_equals_distinct(self):
        result = top_k_frequent([1, 2, 3], 3)
        assert sorted(result) == [1, 2, 3]

    def test_negative_numbers(self):
        result = top_k_frequent([-1, -1, 2, 2, 2, 3], 1)
        assert result == [2]

    def test_random_oracle(self):
        random.seed(42)
        for _ in range(50):
            size = random.randint(1, 100)
            nums = [random.randint(-10, 10) for _ in range(size)]
            distinct = len(set(nums))
            k = random.randint(1, distinct)
            result = top_k_frequent(nums, k)
            assert len(result) == k
            assert len(set(result)) == k
            # verify all returned elements have freq >= any non-returned
            counter = Counter(nums)
            result_set = set(result)
            min_result_freq = min(counter[x] for x in result_set)
            for x in counter:
                if x not in result_set:
                    assert counter[x] <= min_result_freq
