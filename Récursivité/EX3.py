# Tower of Hanoi
def hanoi_moveOne(source, dest):
     print("Move from ", source, " to ", dest)

def hanoi(numberOfDisks, source = "A", dest = "C", aux = "B"):
    if numberOfDisks == 1:
        hanoi_moveOne(source, dest)
    else:
        hanoi(numberOfDisks-1, source, aux, dest)
        hanoi_moveOne(source, dest)
        hanoi(numberOfDisks-1, aux, dest, source)

if __name__ == "__main__":
    hanoi(3)
