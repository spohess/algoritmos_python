def longest_continuous_increasing(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    last_num = -1
    max_count = 1
    last_num = nums[0]
    for num in nums:
        if num > last_num:
            count += 1
        else:
            count = 1

        last_num = num
        if count > max_count:
            max_count = count

    return max_count