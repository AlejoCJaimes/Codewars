def quick_sort(array):
    # first test if the lenght is minus to 1
    if len(array) <= 1:
        return array
    else:
        pivot = array.pop()  # Delete the last element and insert in the var pivot

    # list of divide
    bigger_list = []
    lower_list = []

    for item in array:  # Define order, in my case descending
        if item > pivot:
            bigger_list.append(item)
        else:
            lower_list.append(item)
    return quick_sort(bigger_list) + [pivot] + quick_sort(lower_list)


def diffBig2(array):
    bigger = quick_sort(array)
    return bigger[0] - bigger[1]


if __name__ == '__main__':
    print(diffBig2([10, 5, 2]))
