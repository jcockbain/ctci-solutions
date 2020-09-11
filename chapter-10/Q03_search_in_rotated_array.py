def rotated_search(arr, target):
    return search(arr, target, 0, len(arr) - 1)


def search(nums, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid

    if nums[left] < nums[mid]:
        if nums[left] < target < nums[mid]:
            return search(nums, target, left, mid)
        else:
            return search(nums, target, mid + 1, right)
    elif nums[mid] < nums[right]:
        if nums[mid] < target < nums[right]:
            return search(nums, target, mid + 1, right)
        else:
            return search(nums, target, left, mid)

    else:
        location = -1

        if nums[left] == nums[mid]:
            location = search(nums, target, mid + 1, right)

        if location == -1 and nums[mid] == nums[right]:
            location = search(nums, target, left, mid - 1)

        return location

