"""Bubblesort sorting method."""


def bubblesort(list):
    """Sorting method."""
    num = len(list)

    for i in range(num):
        for j in range(0, num - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
