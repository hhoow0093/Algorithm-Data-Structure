def solve(matrix):
    top = 0
    bottom = len(matrix) - 1
    while top < bottom:
        for i in range(0, len(matrix[0])):
            temp = matrix[top][i]
            matrix[top][i] = matrix[bottom][i]
            matrix[bottom][i] = temp
        top += 1
        bottom -= 1
    for row in range(0, len(matrix)):
        for col in range(row + 1, len(matrix[0])):
            temp = matrix[row][col]
            matrix[row][col] = matrix[col][row]
            matrix[col][row] = temp 
    return matrix

def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = solve(matrix)
    print(result)

main()