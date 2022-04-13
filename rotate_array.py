def rotate(nums: list, k: int) -> None:
    k %= len(nums)
    nums[k:], nums[:k] = nums[:-k], nums[-k:]


num = [1, 2, 3, 4, 5, 6, 7]
rotate(num, k=3)
print(num)
