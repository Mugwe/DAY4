def find_missing(array1, array2):
    array1 = list[45, 65, 1, 3]
    array2 = list[45, 65, 1, 3, 7]

    for element in array1:
        if element not in array2:
            return element
        else:
            return 0

print find_missing
