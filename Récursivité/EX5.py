def EvenOddSort(n, even="", odd=""):
    if n==0:
        print(even+odd)
    if n != 0:
        inp = int(input())
        if inp%2==0:
            EvenOddSort(n-1, even+str(inp)+" ", odd)
        else:
            EvenOddSort(n-1, even, odd+str(inp)+" ")

# test :
if __name__ == "__main__":
    n = int(input())
    EvenOddSort(n)
