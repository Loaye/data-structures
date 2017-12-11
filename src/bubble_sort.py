"""Bubble sort from class"""

def bubble_sort(input_list):
    """Bubble sort function."""
    if isinstance(input, (list)):
        swaps = 1
        while swaps:
            swaps = 0
            for i in range(len(input_list) - 1):
                if input_list[i] > input_list[i + 1]:
                    temp = input_list[i]
                    input_list[i] = input_list[i + 1]
                    input_list[i + 1] = temp
                    swaps += 1
            if swaps == 0:
                return input_list
    else:
        raise TypeError('Function only accepts lists')
