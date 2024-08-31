def recursion(resulting_array, sorted_array, partitions_number, count):

    if len(sorted_array) == partitions_number:  # условие окончания рекурсии
        for j in range(len(sorted_array)):
            resulting_array[count] = sorted_array[j]
            count += 1
        return resulting_array

    length_splin = len(sorted_array) // partitions_number
    del_array = []
    for i in range(partitions_number):
        slice_ = sorted_array[i * length_splin : i * length_splin + length_splin]
        el = slice_[len(slice_) // 2]
        resulting_array[count] = el
        del_array.append(el)
        count += 1
    # удаление текущих 'узлов'
    for k in range(len(del_array)):
        sorted_array.remove(del_array[k])
    return recursion(resulting_array, sorted_array, partitions_number * 2, count)


def GenerateBBSTArray(a):
    sorted_array = sorted(a)
    resulting_array = [None] * len(sorted_array)
    el = sorted_array[len(sorted_array) // 2]
    resulting_array[0] = el
    del sorted_array[len(sorted_array) // 2]  # удаление добавленного узла
    partitions_number = 2
    count = 1
    resulting_list = recursion(resulting_array, sorted_array, partitions_number, count)
    return resulting_list
