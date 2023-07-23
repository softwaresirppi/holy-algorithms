
def binarySearch(items, target):
    begin = 0
    end = len(items)
    while begin < end:
        mid = (begin + end) // 2
        if target < items[mid]:
            end = mid
        elif items[mid] < target:
            begin = mid + 1
        else:
            return mid
    return begin

def binarySearchRecursive(items, begin, end, target):
    if begin < end:
        mid = (begin + end) // 2
        if target < items[mid]:
            return binarySearchRecursive(items, begin, mid, target)
        elif items[mid] < target:
            return binarySearchRecursive(items, mid + 1, end, target)
        else:
            return mid
    return begin


if __name__ == '__main__':
    numbers = [2, 4, 8, 16, 32, 64]
    assert binarySearch(numbers, 8) == 2
    assert binarySearch(numbers, 32) == 4
    assert binarySearch(numbers, 14) == 3
    assert binarySearchRecursive(numbers, 0, len(numbers), 8) == 2
    assert binarySearchRecursive(numbers, 0, len(numbers), 32) == 4
    assert binarySearchRecursive(numbers, 0, len(numbers), 14) == 3
    print(__file__ + ': Passed')
