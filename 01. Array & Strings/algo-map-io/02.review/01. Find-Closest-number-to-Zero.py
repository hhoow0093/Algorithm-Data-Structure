def solve(array):
    distance_minimum = float('inf')
    distance_minimum_arr_num = float('inf')

    for i in range(len(array)):
        distance = abs(array[i])
        if(distance_minimum > distance):
            distance_minimum = distance
            distance_minimum_arr_num = array[i]
        elif(distance == distance_minimum):
            if distance_minimum_arr_num < array[i]:
                distance_minimum = distance
                distance_minimum_arr_num = array[i]
    return distance_minimum_arr_num




def main():
    array = [2, -1, 1]
    result = solve(array)
    print(result)

main()