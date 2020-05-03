def selectionSort(alist):
    for fillslot in range(len(alist)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot+1):
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location
        alist[positionOfMax], alist[fillslot] = alist[fillslot], alist[positionOfMax]

# test :   
alist = [5,4,3,2,1]
selectionSort(alist)
print(alist)
