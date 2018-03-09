def containsNearbyDuplicate(nums, k):
    seen = {}
    for i, num in enumerate(nums):
        if num not in seen:
            seen[num] = i
        else:
            if i - seen[num] <= k:
                return True
            seen[num] = i
    return False
