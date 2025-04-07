
def solve(array_of_nums):
    # o(n)
    # creating left array and right array for generating result
    length = len(array_of_nums)
    # initializing all element in left array to 1
    left_array = []
    for i in range(0, len(array_of_nums)):
        left_array.append(1)
    
    # initializing all elemeent in right array to 1
    right_array = []
    for i in range(0, len(array_of_nums)):
        right_array.append(1)
    
    # creating genuine left array that stores multiplication value to the left side from index -1
    i = 0
    product_left = 1
    while i < length:
        if i == 0:
            i += 1
            continue
        product_left *= array_of_nums[i - 1]
        left_array[i] = product_left
        product_left = left_array[i] 
        i += 1

    i = length - 1
    product_right = 1
    while i > -1:
        if i ==  length - 1:
            i -= 1 
            continue
        product_right *= array_of_nums[i + 1]
        right_array[i] = product_right
        product_right = right_array[i]
        i -= 1
    
    # return the array result by multiplying left and right array
    result = []
    for i in range(0, len(array_of_nums)):
        result.append(right_array[i] * left_array[i])
    return result





def main():
    input_string = input("enter array ',' seperator: ")
    input_string_sanitize = input_string.replace(" ", "")
    input_array_string = input_string_sanitize.split(",")
    input_array_number = list(map(int, input_array_string))
    # input = 1, 2, 3, 4
    solution = solve(input_array_number)
    print(solution)
main()


    # o(n^2)
    # choosen_number = 0
    # solution = []
    # for i in range(0, len(array_of_nums), 1):
    #     solution.append(1)
    
    # i = 0
    # end_loop = len(array_of_nums)
    # while i < end_loop:
    #     j = 0
    #     while j < end_loop:
    #         if j == choosen_number:
    #             solution[i] *= 1
    #         else:
    #             solution[i] *= array_of_nums[j]
    #         j += 1
    #     choosen_number += 1
    #     i += 1
    # return solution