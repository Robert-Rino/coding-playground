
class Solution:
    def heap_sort(self, arr):
        def siftUp(currentIdx, arr):
            parentIdx = (currentIdx-1)//2
            if arr[currentIdx] > arr[parentIdx]:
                swap(currentIdx, parentIdx, arr)
                currentIdx = parentIdx
                siftUp(currentIdx, arr)
            else:
                return

        def siftDown(currentIdx, endIdx, arr):
            while((currentIdx*2)+1 <= endIdx):
                if currentIdx*2 + 2 <= endIdx and arr[currentIdx*2 + 2] > arr[currentIdx*2 + 1]:
                    replaceIdx = currentIdx*2 + 2
                else:
                    replaceIdx = currentIdx*2 + 1

                if arr[currentIdx] < arr[replaceIdx]:
                    swap(currentIdx, replaceIdx, arr)
                    currentIdx = replaceIdx
                    siftDown(currentIdx, endIdx, arr)
                else:
                    break

        def makeMaxHeap(arr):
            last_parent_idx = (len(arr)-2)//2
            for i in reversed(range(last_parent_idx+1)):
                siftDown(i, len(arr)-1, arr)

        def swap(i, j, arr):
            arr[i], arr[j] = arr[j], arr[i]

        makeMaxHeap(arr)
        for i in reversed(range(len(arr))):
            swap(i, 0, arr)
            siftDown(0, i-1, arr)

        return arr
