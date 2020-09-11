def rotated_search(arr, target):
    return search(arr, target, 0, len(arr) - 1)


def search(nums, target, left, right):
    mid = (left + right) // 2

    if nums[mid] == target:
        return mid

    if nums[left] < nums[mid]:
        if nums[left] < target < nums[mid]:
            return search(nums, target, left, mid)
        else:
            return search(nums, target, mid + 1, right)
    elif nums[mid] < nums[right]:
        if nums[right] < target < nums[mid]:
            return search(nums, target, mid + 1, right)
        else:
            return search(nums, target, left, mid)

    return -1
