# Python program: Iterative and Recursive Binary Search
# Date: 2026-08-30

def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    nums = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target = 23
    idx = binary_search_iterative(nums, target)
    print(f"Index of {target}: {idx}")
