# step 1: find the number that starts the sequence by checking if num - 1 in set.
# step 2: if num - 1 not in the set, we found the starting sequence.
# step 3: iterate the founded number by 1 and check if the incremented number exist in the set
# step 4 : if exist, update its length, and if not, update the longest consectutive number between the longesr and the founded length

def solve(nums):
    dict = set(nums)
    longest = 0
    for num in dict:
        number = num
        if number - 1 not in dict:
            length = 1
            while number + 1 in dict:
                length += 1
                number += 1
            if longest < length :
                longest = length
    
    return longest



def main():
    result = solve([-1, 0, 1, 3, 4, 5, 6, 7, 8, 10])
    print(result)

main()