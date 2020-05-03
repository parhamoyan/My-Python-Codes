def insertionSort(alist):
    for index in range(1, len(alist)):
        key = alist[index]
        pos = index-1
        while pos>=0 and alist[pos]>key:
            alist[pos+1] = alist[pos]
            pos -= 1
        alist[pos+1] = key
# test :   
alist = [5,4,3,2,1]
insertionSort (alist)
print(alist)
