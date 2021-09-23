# İkili Arama Algoritması

def BinarySearch(array, search):
    middleIndex = len(array)//2
    lastIndex = len(array)

    if search == array[middleIndex]:
        return middleIndex
    
    elif search > array[middleIndex]:
        for index in range(middleIndex, lastIndex):
            if array[index] == search:
                return index

    else:
        for index in range(middleIndex):
            if array[index] == search:
                return index


print(BinarySearch([4, 8, 18, 97, 107, 109, 340], 107))