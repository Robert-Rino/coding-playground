

def merge_sort(arr, start, end):
    if start < end:
        mid = (start+end)/2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid+1, end)
        merge(arr, start, mid, end)


def merge(arr, start, mid, end):
    left_part = arr[start:mid+1]
    right_part = arr[mid+1:end+1]
    left_part.append(float('inf'))
    right_part.append(float('inf'))

    l_index = 0
    r_index = 0
    for i in range(start, end+1):
        if left_part[l_index] < right_part[r_index]:
            arr[i] = left_part[l_index]
            l_index += 1
        else:
            arr[i] = right_part[r_index]
            r_index += 1

if __name__ == "__main__":
    arr = [5,4,3,2,1,10,8,12]
    merge_sort(arr, 0, len(arr)-1)
    print arr