def solve(matrix):
    # swap top and bottom matrix
    top = 0
    bottom = len(matrix) - 1
    while top < bottom:
        for column in range(0, len(matrix)):
            temp = matrix[top][column]
            matrix[top][column] = matrix[bottom][column]
            matrix[bottom][column] = temp
        top += 1
        bottom -= 1
    # swap using diagonal pivot
    for row in range(0, len(matrix)):
        for col in range(row + 1, len(matrix)):
            temp = matrix[row][col]
            matrix[row][col] = matrix[col][row]
            matrix[col][row] = temp
    return matrix



def main():
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    result = solve(matrix)
    print(result)

main()
