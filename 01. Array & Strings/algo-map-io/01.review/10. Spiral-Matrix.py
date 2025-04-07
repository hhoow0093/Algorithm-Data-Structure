def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    row = len(matrix)
    col = len(matrix[0])

    curr_pos_x = 0
    curr_pos_y = 0

    direction_to_x = 1
    direction_to_y = 0
    # store value of visited points
    visited = []
    for i in range(row * col):
        visited.append(matrix[curr_pos_y][curr_pos_x])
        # to mark the position as alreday visited as .
        matrix[curr_pos_y][curr_pos_x] = "."
        next_y = curr_pos_y + direction_to_y
        next_x = curr_pos_x + direction_to_x
        # out of bounds or visited
        if  next_y >= row or next_x >= col or matrix[next_y][next_x] == ".":
            direction_to_y_temp = direction_to_x
            direction_to_x_temp = -direction_to_y
            direction_to_y = direction_to_y_temp
            direction_to_x = direction_to_x_temp

        curr_pos_x += direction_to_x
        curr_pos_y += direction_to_y

    print(visited)



main()