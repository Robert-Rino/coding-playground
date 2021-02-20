'''
Given a list contains only integers,
move all the zero to end of list,
maintain rest of elements' relative position IN PLACE

eq. input: [1,2,0,6,5,0,10]
    output:[1,2,6,5,10,0,0]
'''

def move_end(array):
    def swap(i, j):
        array[i], array[j] = array[j], array[i]

    for i in range(len(array)):
        if array[i] == 0:
            zero_index = i
            break
        else:
            continue

    if i == len(array) - 1:
        return array

    current_index = zero_index
    while current_index < len(array):
        if array[current_index] != 0:
            swap(zero_index, current_index)
            zero_index += 1
        current_index += 1
    return array


if __name__ == '__main__':
    array = [1,2,0,6,5,0,10]
    print('input:', array)
    print('outpub', move_end(array))
