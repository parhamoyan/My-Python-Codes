def matrix_converter(matrix):
    matrix = matrix[1:len(matrix)]
    level = 0
    start = 0
    end = 0
    res = []
    number = ""
    i = 0
    while i<len(matrix):
        if matrix[i] == "[":
            if level == 0:
                start = i
            level += 1
        elif matrix[i] == "]":
            level -= 1
            if level == 0:
                end = i
                res.append(matrix_converter(matrix[start:end+1]))
        elif matrix[i].isdigit() and level == 0:
            number = matrix[i] + number
            while matrix[i+1].isdigit():
                i += 1
                number += matrix[i]
            res.append(int(number))
            number = ""
        i += 1
    return res

#test :
matrix = "[[1, [[13, 19]]], [112, [3, [4]]]]"
print("input type =", type(matrix))
print("input =", matrix)
matrix = matrix_converter(matrix)
print("output type =", type(matrix))
print("output =", matrix)
