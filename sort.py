# partitions inplace the `items` from begin inclusive to end exclusive.
def partition(items, begin, end):
    pivot = items[end - 1]
    ridge = begin - 1
    for i in range(begin, end):
        if items[i] <= pivot:
            ridge += 1
            items[ridge], items[i] = items[i], items[ridge]
    return ridge

def sort(items, begin, end):
    if begin < end: # the sublist aint empty
        ridge = partition(items, begin, end)
        partition(items, begin, ridge)
        partition(items, ridge + 1, end)

if __name__ == '__main__':
    numbers =[8,4,32,2,64,16]
    sort(numbers, 0, len(numbers))
    assert numbers == [2, 4, 8, 16, 32, 64]
    print(__file__ + ': Passed')
