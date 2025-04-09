def solve(matrix):
    result = []
    dx = 1
    dy = 0
    pos_y = 0
    pos_x = 0
    current = matrix[pos_y][pos_x]
    for _ in range(len(matrix) * len(matrix[0])):
        result.append(current)
        matrix[pos_y][pos_x] = '.'
        
        next_pos_y = pos_y + dy
        next_pos_x = pos_x + dx

        if next_pos_y < 0 or next_pos_y >= len(matrix) or next_pos_x < 0 or next_pos_x >= len(matrix[0]) or matrix[next_pos_y][next_pos_x] == '.':
            dx_temp = -dy
            dy_temp = dx
            dx = dx_temp
            dy = dy_temp 

        pos_y += dy
        pos_x += dx
        current = matrix[pos_y][pos_x]
    return result

def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = solve(matrix)
    print(result)
main()