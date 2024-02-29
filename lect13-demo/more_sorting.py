def merge(listA, listB):
    result = []
    i = j = 0
    while i < len(listA) and j < len(listB):
        if listA[i] < listB[j]:
            result.append(listA[i])
            i += 1
        else:
            result.append(listB[j])
            j += 1

    while i < len(listA):
        result.append(listA[i])
        i += 1

    while j < len(listB):
        result.append(listB[j])
        j += 1
    return result

listA = [1,2,3]
listB = [4,5,6]
print(merge(listA, listB))