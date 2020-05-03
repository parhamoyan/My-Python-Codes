def shortBubbleSort(alist):
    passnum = len(alist)-1
    exchanges = True
    while passnum>0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                exchanges = True
        passnum -= 1

# test :   
alist = [5,4,3,2,1]
shortBubbleSort(alist)
print(alist)
