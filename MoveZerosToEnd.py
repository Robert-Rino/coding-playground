'''
Given a list contains only integers,
move all the zero to end of list,
maintain rest of elements' relative position IN PLACE

eq. input: [1,2,0,6,5,0,10]
    output:[1,2,6,5,10,0,0]
'''

def move_end(array):
    count = 0
    for n in array:
        if n == 0:
            count += 1

    array[:] =[i for i in array if i!=0 ]
    array += [0]*count

if __name__ == '__main__':
    array = [1,2,0,6,5,0,10]
    move_end(array)
    print array