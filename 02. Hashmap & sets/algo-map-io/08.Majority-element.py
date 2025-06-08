# step 1 : create a new dictionary with each key counts the number of occurences in the array
# step 2 : generate 2 arrays. 1 for storing keys, and other is for storing values
# step 3 : calculate the largest value from the value list, take the index. 
# step 4 : print the key based from the given index from step 3

def solve(nums):
    dict = {}

    for i in range(0, len(nums)):
        if nums[i] not in dict:
            dict[nums[i]] = 1
        else:
            dict[nums[i]] += 1

    values = list(dict.values())
    key = list(dict.keys())
    max = float('-inf')
    index = 0
    for i in range(0, len(values)):
        if max < values[i]:
            max = values[i]
            index = i
    return key[index]

def main():
    print(solve([3,2,3]))

main()
