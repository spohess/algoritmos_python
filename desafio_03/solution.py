def remove_duplicates(nums: list[int]) -> list[int]:
    result = []
    for num in nums:
        find = False
        for selected in result:
            if num == selected:
                find = True
                break
        if not find:
            result.append(num)
    
    return result
