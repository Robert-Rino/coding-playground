'''
Given a list contains only integers,
move all the zero to end of list,
maintain rest of elements' relative position IN PLACE

eq. input: [1,2,0,6,5,0,10]
    output:[1,2,6,5,10,0,0]
'''

def move_end(array):
    currentIdx = 0
    zeroIdx = -1
    while(currentIdx < len(array)):
        if array[currentIdx] != 0:
            if zeroIdx != -1:
                array[currentIdx], array[zeroIdx] = array[zeroIdx], array[currentIdx]
                zeroIdx = currentIdx
            currentIdx = currentIdx + 1

        else:
            if zeroIdx == -1:
                zeroIdx = currentIdx
            else:
                pass

            currentIdx += 1

if __name__ == '__main__':
    array = [1,2,0,6,5,0,10]
    move_end(array)
    print array