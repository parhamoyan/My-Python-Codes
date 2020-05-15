def bubblesSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

# test :   
alist = [5,4,3,2,1]
bubblesSort(alist)
print(alist)
