def has_pair_with_sum(nums: list[int], target: int) -> bool:
    """Verifica se existe um par de números cuja soma é target."""
    for index_main, item_main in enumerate(nums):
        for index_sec, item_sec in enumerate(nums):
            if index_main == index_sec:
                continue
            if item_main + item_sec == target:
                return True

    return False
