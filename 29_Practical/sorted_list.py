def _sort(unsorted: list) -> list:
    indexes = [i for i in range(len(unsorted)) if unsorted[i] == -1]

    unsorted = [unsorted[i] for i in range(len(unsorted)) if i not in indexes]

    unsorted.sort()
    for i in indexes:
        unsorted.insert(i, -1)

    return unsorted


unsorted = [-1, 150, 190, 170, -1, -1, 160, 180]
sorted = _sort(unsorted)
print(sorted)