def reverse(n):
    if n != 0:
        inp = input()
        reverse(n-1)
        print(inp)

# test :
if __name__ == "__main__":
    n = int(input())
    reverse(n)
