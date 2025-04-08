def solve(array):
    # create leftside array
    left_array = []
    initial_product = 1
    for i in range(0, len(array)):
        if i == 0:
            left_array.append(1)
        else:
            add = array[i - 1] * initial_product
            left_array.append(add)
            initial_product = add
    
    # create rightside array
    right_array = []
    # initialize all right value with 1 as big as array
    for _ in range(0, len(array)):
        right_array.append(1)
    
    #build right side array
    initial_product = 1
    for i in range(len(array) - 1, -1, -1):
        if i == len(array) - 1:
            continue
        else:
            modify = array[i + 1] * initial_product
            right_array[i] = modify
            initial_product = modify
    
    # we can finally build the resulr array
    result = []
    for i in range(0, len(array)):
        result.append(right_array[i] * left_array[i])
    return result



def main():
    array = [1, 2, 3, 4]
    result = solve(array)
    print(result)
main()