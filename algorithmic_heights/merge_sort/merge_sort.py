
def merge_sort(array1,array2):
    if array1 == []:
        return array2
    elif array2 == []:
        return array1
    elif array1[0] < array2:
        return array1[0] + merge_sort(array1[:1],array2)
    elif array1[0] > array2:
        return array2[0] + merge_sort(array1,array2[:1])
    elif array1[0] == array2[0]:
        return array1[0] + array2[0] + merge_sort(array1[:1],array2[:1])
    else:
        return 0
                

